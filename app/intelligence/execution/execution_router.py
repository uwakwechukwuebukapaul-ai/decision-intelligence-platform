"""
Execution Router

Routes decision requests to the
appropriate runtime capability.
"""

from __future__ import annotations

from app.intelligence.fabric.engine_registry import EngineRegistry


class ExecutionRouter:
    """
    Enterprise execution router.

    Responsible for locating the
    appropriate intelligence engine.
    """

    def __init__(self):

        self.registry = EngineRegistry()

    def resolve(
        self,
        capability: str,
    ):

        return self.registry.get_engine(
            capability
        )

    def has_capability(
        self,
        capability: str,
    ) -> bool:

        return (
            self.resolve(capability)
            is not None
        )

    def available_capabilities(
        self,
    ):

        return sorted(
            self.registry.available_capabilities()
        )