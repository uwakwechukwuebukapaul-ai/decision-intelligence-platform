"""
Intelligence Kernel

Central orchestration layer for all intelligence execution.

Responsibilities
----------------
1. Validate incoming requests
2. Create execution context
3. Execute governance checks
4. Invoke intelligence runtime
5. Capture execution telemetry
6. Build standardized responses

All future intelligence capabilities should execute through this
kernel instead of calling engines directly.
"""

from __future__ import annotations

from typing import Any

from app.intelligence.kernel.execution_context import ExecutionContext
from app.intelligence.kernel.request_validator import RequestValidator
from app.intelligence.kernel.response_builder import ResponseBuilder


class IntelligenceKernel:
    """
    Central intelligence orchestration component.

    The kernel does not implement intelligence itself.

    It coordinates execution between platform components while
    remaining independent from specific reasoning engines.
    """

    def __init__(
        self,
        runtime: Any | None = None,
        governance: Any | None = None,
    ) -> None:

        self.runtime = runtime
        self.governance = governance

    def execute(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute an intelligence request.
        """

        #
        # Step 1
        # Validate request
        #

        validation = RequestValidator.validate(payload)

        if not validation.valid:

            return ResponseBuilder.validation_error(
                validation.message
            )

        #
        # Step 2
        # Create execution context
        #

        context = ExecutionContext(
            user_id=payload["user_id"],
            capability=payload["capability"],
            objective=payload.get("objective"),
        )

        context.add_trace(
            "Execution context created."
        )

        #
        # Step 3
        # Governance
        #

        if self.governance is not None:

            try:

                governance_result = (
                    self.governance.evaluate(
                        context
                    )
                )

                context.add_governance_result(
                    "evaluation",
                    governance_result,
                )

                context.add_trace(
                    "Governance evaluation completed."
                )

            except Exception as exc:

                context.add_trace(
                    f"Governance error: {exc}"
                )

                return ResponseBuilder.failure(
                    context=context,
                    message="Governance evaluation failed.",
                    error_code="GOVERNANCE_ERROR",
                    details=str(exc),
                )

        #
        # Step 4
        # Runtime execution
        #

        if self.runtime is None:

            result = {
                "capability": context.capability,
                "objective": context.objective,
                "message": (
                    "No runtime configured."
                ),
            }

            context.add_trace(
                "Execution completed without runtime."
            )

            return ResponseBuilder.success(
                context=context,
                result=result,
            )

        try:

            context.add_trace(
                "Invoking runtime."
            )

            runtime_result = self.runtime.execute(
                context=context,
                capability=context.capability,
                objective=context.objective,
                metadata=context.metadata,
            )

            context.add_trace(
                "Runtime completed successfully."
            )

            return ResponseBuilder.success(
                context=context,
                result=runtime_result,
            )

        except Exception as exc:

            context.add_trace(
                f"Runtime failure: {exc}"
            )

            return ResponseBuilder.failure(
                context=context,
                message="Runtime execution failed.",
                error_code="RUNTIME_ERROR",
                details=str(exc),
            )