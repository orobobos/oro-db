"""Public interface for oro-db.

Re-exports the primary types and functions that consumers should use.
"""

from oro_db.config import CoreSettings, get_config, set_config
from oro_db.db import (
    AsyncConnectionPool,
    ConnectionPool,
    async_cursor,
    get_connection,
    get_cursor,
    put_connection,
)
from oro_db.exceptions import (
    ConfigError,
    ConflictError,
    DatabaseError,
    NotFoundError,
    OroDbError,
    ValidationError,
)
from oro_db.migrations import MigrationRunner

__all__ = [
    # Config
    "CoreSettings",
    "get_config",
    "set_config",
    # DB
    "ConnectionPool",
    "AsyncConnectionPool",
    "get_cursor",
    "async_cursor",
    "get_connection",
    "put_connection",
    # Exceptions
    "OroDbError",
    "DatabaseError",
    "ValidationError",
    "ConfigError",
    "NotFoundError",
    "ConflictError",
    # Migrations
    "MigrationRunner",
]
