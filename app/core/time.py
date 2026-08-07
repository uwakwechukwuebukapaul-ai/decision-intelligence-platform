"""
Sentinel DNA - Time Utilities

Centralized timezone-aware datetime helpers.

Purpose:
- Remove deprecated datetime.utcnow() usage
- Provide consistent UTC timestamps
- Standardize timestamps across enterprise modules
"""

from datetime import datetime, UTC


def utc_now() -> datetime:
    """
    Return current timezone-aware UTC datetime.
    """
    return datetime.now(UTC)


def utc_timestamp() -> str:
    """
    Return current UTC timestamp in ISO format.
    """
    return datetime.now(UTC).isoformat()