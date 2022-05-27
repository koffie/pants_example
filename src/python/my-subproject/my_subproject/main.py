"""my_subproject entrypoint.

This module is the entrypoint of the my_subproject package.
"""

import asyncio  # noqa: F401
import logging  # noqa: F401

from my_subproject.core.config import settings  # noqa: F401


def run() -> None:
    pass


if __name__ == "__main__":
    """Start the ZMQ application."""
    run()
