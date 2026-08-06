"""
Enterprise Intelligence Pipeline.

Coordinates execution of intelligence processing stages.
"""

from __future__ import annotations

from typing import Any, Dict, List

from app.intelligence.pipeline.pipeline_result import PipelineResult
from app.intelligence.pipeline.pipeline_stage import PipelineStage
from app.intelligence.pipeline.stage_executor import StageExecutor


class IntelligencePipeline:
    """
    Executes registered pipeline stages in order.

    The pipeline is intentionally fail-fast:
    execution stops immediately if a stage fails.
    """

    def __init__(self) -> None:
        self._stages: List[PipelineStage] = []
        self._executor = StageExecutor()

    @property
    def stages(self) -> List[PipelineStage]:
        """Return registered stages."""
        return list(self._stages)

    def register_stage(self, stage: PipelineStage) -> None:
        """
        Register a pipeline stage.

        Parameters
        ----------
        stage:
            Stage implementation.
        """
        self._stages.append(stage)

    def clear(self) -> None:
        """Remove all registered stages."""
        self._stages.clear()

    def execute(self, context: Dict[str, Any]) -> PipelineResult:
        """
        Execute the full intelligence pipeline.

        Parameters
        ----------
        context:
            Shared execution context.

        Returns
        -------
        PipelineResult
        """
        current_context = dict(context)

        if not self._stages:
            return PipelineResult.success_result(
                stage="pipeline",
                context=current_context,
                message="Pipeline completed (no stages registered).",
            )

        for stage in self._stages:

            result = self._executor.execute(
                stage=stage,
                context=current_context,
            )

            if not result.success:
                return result

            current_context = result.context

        return PipelineResult.success_result(
            stage="pipeline",
            context=current_context,
            message="Pipeline completed successfully.",
        )