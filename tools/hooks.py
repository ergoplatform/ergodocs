import logging
import os
import pathlib
import re
from collections import defaultdict
from urllib.parse import quote

LOG = logging.getLogger(__name__)

_FENCE = re.compile(r"^[ \t]*(```|~~~)")
_LIST_ITEM = re.compile(r"^([ \t]*)([*+-]|\d+\.)[ \t]+")
_CARD_URL_JSON = re.compile(r'("url"\s*:\s*")([^"/:#][^"#]*\.md)(#[^"]*)?(")')
_CARD_URL_YAML = re.compile(r"(\burl:\s*)([^/\s:#][^\s#]*\.md)(#[^\s]*)?")


def _indent_width(prefix: str) -> int:
    # tabs inside Markdown list indentation are ambiguous; normalize to spaces.
    return len(prefix.expandtabs(2))


def _filename_index(files):
    index = defaultdict(list)
    for file_ in files:
        if getattr(file_, "abs_src_path", None):
            index[os.path.basename(file_.abs_src_path)].append(file_.abs_src_path)
    return index


def _relative_doc_link(target: str, anchor: str, page, files) -> str:
    index = _filename_index(files)
    if target not in index:
        return target + (anchor or "")

    matches = index[target]
    if len(matches) > 1:
        LOG.warning("Card URL '%s' matches multiple docs: %s", target, matches)

    page_dir = os.path.dirname(page.file.abs_src_path)
    rel = pathlib.PurePath(os.path.relpath(matches[0], page_dir)).as_posix()
    return quote(rel) + (anchor or "")


def _fix_card_urls(markdown: str, page=None, files=None, **kwargs) -> str:
    if page is None or files is None:
        return markdown

    def json_repl(match):
        target = _relative_doc_link(match.group(2), match.group(3), page, files)
        return f"{match.group(1)}{target}{match.group(4)}"

    def yaml_repl(match):
        target = _relative_doc_link(match.group(2), match.group(3), page, files)
        return f"{match.group(1)}{target}"

    markdown = _CARD_URL_JSON.sub(json_repl, markdown)
    return _CARD_URL_YAML.sub(yaml_repl, markdown)


def fix_lists(markdown: str, **kwargs) -> str:
    """
    Normalize over-indented nested list markers to play well with
    mdx_truly_sane_lists (nested_indent=2).

    This keeps existing 2-space nesting intact while repairing common 4/6-space
    nesting patterns that otherwise get flattened into a paragraph.
    """
    lines = markdown.splitlines()
    out = []

    in_fence = False
    # Track source and output indents separately so siblings with legacy
    # indentation stay at the same logical depth after normalization.
    src_stack = []
    out_stack = []

    for line in lines:
        if _FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            out.append(line)
            continue

        match = _LIST_ITEM.match(line)
        if match:
            src_indent_text = match.group(1)
            src_indent = _indent_width(src_indent_text)

            while src_stack and src_indent <= src_stack[-1]:
                src_stack.pop()
                out_stack.pop()

            if src_stack:
                parent_src_indent = src_stack[-1]
                parent_out_indent = out_stack[-1]
                if src_indent - parent_src_indent >= 2:
                    out_indent = parent_out_indent + 2
                else:
                    out_indent = src_indent
            else:
                out_indent = src_indent

            if out_indent != src_indent:
                line = (" " * out_indent) + line[len(src_indent_text):]

            src_stack.append(src_indent)
            out_stack.append(out_indent)
            out.append(line)
            continue

        current_indent = _indent_width(line[: len(line) - len(line.lstrip(" \t"))])
        while src_stack and current_indent < src_stack[-1]:
            src_stack.pop()
            out_stack.pop()

        out.append(line)

    return _fix_card_urls("\n".join(out), **kwargs)
