"""my_subproject."""

from importlib.metadata import PackageNotFoundError, version

__version__ = version(__name__)

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    pass
