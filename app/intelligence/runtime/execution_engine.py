"""
Execution Engine

Enterprise runtime execution layer.
"""

from __future__ import annotations

import time

from .execution_context import ExecutionContext
from .execution_result import ExecutionResult
from .execution_history import ExecutionHistory
from .runtime_events import RuntimeEvents
from .engine_dispatcher import EngineDispatcher
from .job import IntelligenceJob


class ExecutionEngine:

    def __init__(self):

        self.dispatcher = EngineDispatcher()

        self.history = ExecutionHistory()

        self.events = RuntimeEvents()

    def execute(
        self,
        job: IntelligenceJob,
    ) -> ExecutionResult:

        context = ExecutionContext(
            job_id=job.job_id,
            capability=job.capability,
            payload=job.payload,
        )

        self.events.emit(
            RuntimeEvents.JOB_STARTED,
            context.execution_id,
        )

        started = time.perf_counter()

        try:

            output = self.dispatcher.dispatch(
                context
            )

            duration = (
                time.perf_counter() - started
            ) * 1000

            result = ExecutionResult(
                execution_id=context.execution_id,
                success=True,
                status="completed",
                engine=context.capability,
                output=output,
                duration_ms=duration,
            )

            self.history.record(result)

            self.events.emit(
                RuntimeEvents.JOB_COMPLETED,
                context.execution_id,
            )

            job.complete()

            return result

        except Exception as exc:

            duration = (
                time.perf_counter() - started
            ) * 1000

            result = ExecutionResult(
                execution_id=context.execution_id,
                success=False,
                status="failed",
                engine=context.capability,
                error=str(exc),
                duration_ms=duration,
            )

            self.history.record(result)

            self.events.emit(
                RuntimeEvents.JOB_FAILED,
                context.execution_id,
                {
                    "error": str(exc)
                },
            )

            job.fail()

            return result