"""Simple offline-friendly breadcrumbs plugin for MkDocs."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.nav import Navigation
from mkdocs.structure.pages import Page


Breadcrumb = Dict[str, Optional[str]]


class BreadcrumbsPlugin(BasePlugin):
    """Populate template context with breadcrumb links."""

    config_scheme = (
        ("include_home", config_options.Type(bool, default=True)),
    )

    def on_page_context(
        self,
        context: Dict[str, Any],
        page: Page,
        config: Dict[str, Any],
        nav: Navigation,
        **_: Any,
    ) -> Dict[str, Any]:
        """Attach breadcrumb data to the current page context."""

        breadcrumbs = self._build_breadcrumbs(page, nav)
        context["breadcrumbs"] = breadcrumbs
        # Expose breadcrumbs through page metadata for templates or markdown.
        page.meta.setdefault("breadcrumbs", breadcrumbs)
        return context

    def _build_breadcrumbs(self, page: Page, nav: Navigation) -> List[Breadcrumb]:
        """Generate breadcrumb dictionaries for template rendering."""

        crumbs: List[Breadcrumb] = []

        if self.config.get("include_home", True) and getattr(nav, "homepage", None):
            home = nav.homepage
            if home and home.url != page.url:
                crumbs.append({"title": home.title or "Home", "url": home.url})

        for ancestor in getattr(page, "ancestors", []):
            url = getattr(ancestor, "url", None)
            if url == page.url:
                url = None
            crumbs.append({"title": ancestor.title, "url": url})

        crumbs.append({"title": page.title, "url": None})
        return crumbs
