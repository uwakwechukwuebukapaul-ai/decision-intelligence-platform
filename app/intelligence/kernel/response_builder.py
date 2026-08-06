"""
Response Builder

Builds standardized intelligence execution responses.

All intelligence execution should return responses through this builder
to guarantee a consistent API contract across the platform.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from app.intelligence.kernel.execution_context import ExecutionContext


class ResponseBuilder:
    """
    Standard response builder for intelligence execution.

    Responsibilities
    ----------------
    - Success responses
    - Error responses
    - Consistent response schema
    - Execution metadata
    """

    @staticmethod
    def success(
        context: ExecutionContext,
        result: Any,
        message: str = "Execution completed successfully.",
    ) -> dict[str, Any]:
        """
        Build a successful execution response.
        """

        return {
            "status": "success",
            "message": message,
            "execution": {
                "execution_id": context.execution_id,
                "correlation_id": context.correlation_id,
                "user_id": context.user_id,
                "capability": context.capability,
                "objective": context.objective,
                "created_at": context.created_at.isoformat(),
            },
            "result": result,
            "metadata": context.metadata,
            "runtime_metrics": context.runtime_metrics,
            "governance": context.governance,
            "decision_trace": context.decision_trace,
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }

    @staticmethod
    def failure(
        context: ExecutionContext | None,
        message: str,
        error_code: str = "EXECUTION_ERROR",
        details: Any = None,
    ) -> dict[str, Any]:
        """
        Build a failed execution response.
        """

        execution = None

        if context is not None:

            execution = {
                "execution_id": context.execution_id,
                "correlation_id": context.correlation_id,
                "user_id": context.user_id,
                "capability": context.capability,
                "objective": context.objective,
                "created_at": context.created_at.isoformat(),
            }

        return {
            "status": "error",
            "error": {
                "code": error_code,
                "message": message,
                "details": details,
            },
            "execution": execution,
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }

    @staticmethod
    def validation_error(
        message: str,
    ) -> dict[str, Any]:
        """
        Standard validation error response.
        """

        return {
            "status": "error",
            "error": {
                "code": "VALIDATION_ERROR",
                "message": message,
            },
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }

    @staticmethod
    def capability_not_found(
        capability: str,
    ) -> dict[str, Any]:
        """
        Capability lookup failure.
        """

        return {
            "status": "error",
            "error": {
                "code": "CAPABILITY_NOT_FOUND",
                "message": (
                    f"Capability '{capability}' "
                    "is not registered."
                ),
            },
            "generated_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }