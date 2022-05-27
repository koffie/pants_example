"""my_subproject core configuration.

This module contains the configuration for the core functionality of the
my_subproject package.
"""

import secrets  # noqa: F401
from typing import Any, Dict, List, Optional, Union  # noqa: F401

from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        case_sensitive = True


settings = Settings()
