"""Monkey-patch for django.template.context.BaseContext.__copy__.

Some Django installs (or Python versions) may expose a broken implementation
that attempts to copy `super()` itself. This patch provides a safe
implementation that creates a shallow duplicate and copies the `dicts` list.
"""
from copy import copy as _copy

def _basecontext_copy(self):
    # Create a new instance without calling __init__
    cls = self.__class__
    duplicate = object.__new__(cls)

    # Copy instance dict if present (safely)
    if hasattr(self, "__dict__"):
        duplicate.__dict__.update(self.__dict__)

    # Make sure `dicts` is a shallow copy (so modifications don't affect the original)
    duplicate.dicts = list(self.dicts)
    return duplicate


def apply_patch():
    try:
        from django.template import context as _ctx
    except Exception:
        return False

    # Replace BaseContext.__copy__ only if it's necessary
    try:
        _ctx.BaseContext.__copy__ = _basecontext_copy
        return True
    except Exception:
        return False
