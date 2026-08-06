"""
Core Platform Infrastructure
"""

from .container import (
    ServiceContainer,
    ServiceContainer as Container,
    container,
)

from .runtime import (
    IntelligenceRuntime,
)

from .application import (
    ApplicationRuntime,
    runtime,
)


__all__ = [
    "Container",
    "ServiceContainer",
    "container",
    "IntelligenceRuntime",
    "ApplicationRuntime",
    "runtime",
]