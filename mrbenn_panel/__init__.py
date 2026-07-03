# Import the panel lazily. Importing it eagerly here would, while Django is
# still populating INSTALLED_APPS, pull in debug_toolbar's panel stack -- which
# under django-debug-toolbar >= 7 imports a database model (HistoryEntry) at
# import time and raises AppRegistryNotReady. Keeping ``from mrbenn_panel import
# MrBennPanel`` working via PEP 562 avoids that without changing the public API.


def __getattr__(name):
    if name == "MrBennPanel":
        from mrbenn_panel.panel import MrBennPanel

        return MrBennPanel
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
