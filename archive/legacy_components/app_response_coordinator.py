"""
Incident Response Compatibility Adapter

The ResponseCoordinator implementation lives in:
services.response_engine.response_coordinator

This module exists only to preserve legacy imports.
"""

from services.response_engine.response_coordinator import ResponseCoordinator


__all__ = [
    "ResponseCoordinator"
]