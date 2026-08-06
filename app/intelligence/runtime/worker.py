"""
Runtime Worker

Executes runtime jobs through the execution engine.
"""

from __future__ import annotations

from .execution_engine import ExecutionEngine
from .job import IntelligenceJob
from .execution_result import ExecutionResult


class Worker:
    """
    Runtime worker.

    Future implementations may execute jobs
    using threads, asyncio, Celery, or Kubernetes.
    """

    def __init__(
        self,
        execution_engine: ExecutionEngine,
    ):

        self.execution_engine = execution_engine

    def run(
        self,
        job: IntelligenceJob,
    ) -> ExecutionResult:

        return self.execution_engine.execute(job)