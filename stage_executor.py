from __future__ import annotations

from app.intelligence.pipeline.pipeline_result import PipelineResult
from app.intelligence.pipeline.pipeline_stage import PipelineStage


class StageExecutor:
    """
    Executes a single pipeline stage.

    The executor is intentionally lightweight. It simply invokes the
    stage, ensures a PipelineResult is returned, and converts any
    unexpected exception into a failed PipelineResult.
    """

    def execute(
        self,
        stage: PipelineStage,
        context: dict,
    ) -> PipelineResult:
        try:
            result = stage.execute(context)

            # Backward compatibility: allow stages to return the
            # updated context directly.
            if isinstance(result, dict):
                return PipelineResult(
                    success=True,
                    stage=stage.name,
                    context=result,
                )

            if isinstance(result, PipelineResult):
                return result

            raise TypeError(
                f"{stage.__class__.__name__}.execute() "
                "must return PipelineResult or dict."
            )

        except Exception as exc:
            return PipelineResult(
                success=False,
                stage=stage.name,
                message=str(exc),
                context=context,
                metadata={
                    "exception_type": type(exc).__name__,
                },
            )