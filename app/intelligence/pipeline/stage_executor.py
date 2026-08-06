"""
Stage Executor.

Executes a single Intelligence Pipeline stage.
"""

from __future__ import annotations

from typing import Any, Dict

from app.intelligence.pipeline.pipeline_result import PipelineResult
from app.intelligence.pipeline.pipeline_stage import PipelineStage


class StageExecutor:
    """
    Executes a pipeline stage and normalizes its output.

    Supported stage return values:
        - PipelineResult
        - dict (updated context)

    Any exception is converted into a failed PipelineResult.
    """

    def execute(
        self,
        stage: PipelineStage,
        context: Dict[str, Any],
    ) -> PipelineResult:
        """
        Execute one stage.

        Parameters
        ----------
        stage:
            Pipeline stage.

        context:
            Shared execution context.

        Returns
        -------
        PipelineResult
        """

        try:
            result = stage.execute(dict(context))

            # ---------------------------------------------------------
            # Stage already returned a PipelineResult.
            # Do NOT wrap it again.
            # ---------------------------------------------------------
            if isinstance(result, PipelineResult):
                return result

            # ---------------------------------------------------------
            # Stage returned an updated context dictionary.
            # ---------------------------------------------------------
            if isinstance(result, dict):
                return PipelineResult.success_result(
                    stage=stage.name,
                    context=result,
                )

            raise TypeError(
                f"{stage.__class__.__name__}.execute() must return "
                "PipelineResult or dict."
            )

        except Exception as exc:
            return PipelineResult.failure_result(
                stage=stage.name,
                message=str(exc),
                context=dict(context),
                metadata={
                    "exception_type": type(exc).__name__,
                },
            )