import importlib.util

from my_subproject2 import __version__


def test_installed() -> None:
    spec = importlib.util.find_spec("my_submodule")
    assert spec is not None
    # assert "site-packages" in spec.origin


def test_version() -> None:
    assert __version__ == "0.1.0"
