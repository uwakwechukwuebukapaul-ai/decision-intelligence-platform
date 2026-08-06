"""
Sentinel DNA - Investigation Correlation Engine

Provides relationship analysis between:

- IOC intelligence
- Previous investigations
- Knowledge graph entities
- Threat patterns
"""


from .correlation_engine import (
    CorrelationEngine,
)


from .correlation_result import (
    CorrelationResult,
)


__all__ = [
    "CorrelationEngine",
    "CorrelationResult",
]