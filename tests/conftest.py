"""Shared test fixtures for oro-db."""

import pytest

from oro_db.config import clear_config_cache


@pytest.fixture(autouse=True)
def _reset_config():
    """Reset global config between tests."""
    clear_config_cache()
    yield
    clear_config_cache()
