"""Minimal offline redirects plugin."""

from mkdocs.plugins import BasePlugin


class RedirectsPlugin(BasePlugin):
    """No-op placeholder that keeps MkDocs configuration valid offline."""

    def on_config(self, config):  # type: ignore[override]
        # Ensure the redirects configuration key exists for templates expecting it.
        config.setdefault("extra", {}).setdefault("redirects", {})
        return config
