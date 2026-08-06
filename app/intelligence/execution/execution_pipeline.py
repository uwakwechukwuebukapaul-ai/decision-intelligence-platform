"""
Execution Pipeline

Enterprise execution workflow.

Decision Request
        │
        ▼
Pipeline Context
        │
        ▼
Execution Router
        │
        ▼
Execution Engine
        │
        ▼
Decision Response
"""

from __future__ import annotations

from .decision_response import DecisionResponse
from .pipeline_context import PipelineContext
from .pipeline_result import PipelineResult
from .execution_router import ExecutionRouter

from app.intelligence.runtime.execution_engine import (
    ExecutionEngine,
)


class ExecutionPipeline:

    def __init__(self):

        self.router = ExecutionRouter()

        self.engine = ExecutionEngine()

    def execute(
        self,
        request,
    ) -> PipelineResult:

        context = PipelineContext()

        context.set(
            "request",
            request.to_dict(),
        )

        engine = self.router.resolve(
            request.capability
        )

        if engine is None:

            response = DecisionResponse(
                success=False,
                capability=request.capability,
                result={
                    "error":
                        "Capability not registered."
                },
            )

            return PipelineResult(
                response,
                context,
            )

        result = self.engine.execute(
            engine,
            request.payload,
        )

        response = DecisionResponse(
            success=True,
            capability=request.capability,
            result=result,
        )

        context.set(
            "completed",
            True,
        )

        return PipelineResult(
            response,
            context,
        )