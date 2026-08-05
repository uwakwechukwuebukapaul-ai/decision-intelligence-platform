"""
Legacy ResponseCoordinator Compatibility Wrapper

Redirects old imports to the canonical response engine implementation.
"""


from services.response_engine.response_coordinator import ResponseCoordinator


__all__ = [
    "ResponseCoordinator"
]