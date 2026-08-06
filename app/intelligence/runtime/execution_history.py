"""
Execution History

Stores completed runtime executions.
"""

from __future__ import annotations

from .execution_result import ExecutionResult


class ExecutionHistory:
    """
    In-memory execution history.

    Future versions can replace the internal
    storage with SQLite/PostgreSQL without
    changing callers.
    """

    def __init__(self):

        self._history: list[ExecutionResult] = []

    def record(
        self,
        result: ExecutionResult,
    ) -> None:

        self._history.append(result)

    def all(self) -> list[ExecutionResult]:

        return list(self._history)

    def latest(self) -> ExecutionResult | None:

        if not self._history:
            return None

        return self._history[-1]

    def count(self) -> int:

        return len(self._history)

    def clear(self) -> None:

        self._history.clear()