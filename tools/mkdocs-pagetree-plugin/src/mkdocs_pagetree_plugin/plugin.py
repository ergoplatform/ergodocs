"""Simple offline page tree plugin for MkDocs."""

from __future__ import annotations

from typing import List

from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Navigation
from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page


class PageTreePlugin(BasePlugin):
    """Render the site navigation as a nested Markdown list."""

    def __init__(self) -> None:
        self._nav: Navigation | None = None

    def on_nav(self, nav: Navigation, config, files):  # type: ignore[override]
        self._nav = nav
        return nav

    def on_page_markdown(self, markdown: str, page: Page, config, files):  # type: ignore[override]
        if "<pagetree" not in markdown:
            return markdown
        tree = self._render_tree()
        return markdown.replace("<pagetree />", tree).replace("<pagetree/>", tree)

    def _render_tree(self) -> str:
        if not self._nav:
            return ""
        lines: List[str] = []
        for item in self._nav.items:
            self._render_item(item, lines, 0)
        return "\n".join(lines) + "\n"

    def _render_item(self, item, lines: List[str], depth: int) -> None:
        indent = "  " * depth
        title = getattr(item, "title", "")
        url = None
        if isinstance(item, Page) and getattr(item, "file", None):
            url = item.file.src_path.replace('\\', '/')
        else:
            raw_url = getattr(item, "url", None)
            if raw_url:
                url = raw_url
        if isinstance(item, Section):
            lines.append(f"{indent}- **{title}**")
            for child in item.children:
                self._render_item(child, lines, depth + 1)
        else:
            if not title:
                return
            if url:
                lines.append(f"{indent}- [{title}]({url})")
            else:
                lines.append(f"{indent}- {title}")
            if getattr(item, "children", None):
                for child in item.children:
                    self._render_item(child, lines, depth + 1)
