import re

_FENCE = re.compile(r"^[ \t]*(```|~~~)")
_LIST_ITEM = re.compile(r"^([ \t]*)([*+-]|\d+\.)[ \t]+")


def _indent_width(prefix: str) -> int:
    # tabs inside Markdown list indentation are ambiguous; normalize to spaces.
    return len(prefix.expandtabs(2))


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

    return "\n".join(out)
