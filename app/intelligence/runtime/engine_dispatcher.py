"""
Engine Dispatcher

Routes runtime jobs to the appropriate
intelligence engine.
"""

from __future__ import annotations

from .execution_context import ExecutionContext


class EngineDispatcher:
    """
    Runtime capability dispatcher.
    """

    def __init__(self):

        self._engines: dict[str, callable] = {}

    def register(
        self,
        capability: str,
        handler,
    ) -> None:

        self._engines[capability] = handler

    def registered_capabilities(self) -> list[str]:

        return sorted(
            self._engines.keys()
        )

    def dispatch(
        self,
        context: ExecutionContext,
    ) -> dict:

        handler = self._engines.get(
            context.capability
        )

        if handler is None:

            raise ValueError(
                f"No engine registered for capability "
                f"'{context.capability}'."
            )

        return handler(context)

    def has_engine(
        self,
        capability: str,
    ) -> bool:

        return capability in self._engines

    def unregister(
        self,
        capability: str,
    ) -> None:

        self._engines.pop(
            capability,
            None,
        )

    def clear(self) -> None:

        self._engines.clear()