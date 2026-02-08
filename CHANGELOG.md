# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial extraction from valence core
- `ConnectionPool` with thread-safe psycopg2 pool management
- `AsyncConnectionPool` with asyncpg async pool management
- `get_cursor()` and `async_cursor()` context managers
- `CoreSettings` configuration via pydantic-settings
- Exception hierarchy: `ValenceException`, `DatabaseException`, `ValidationException`, etc.
- `MigrationRunner` for versioned database migrations
- `escape_ilike()` utility for safe SQL pattern matching
