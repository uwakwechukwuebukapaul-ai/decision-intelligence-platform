"""
Pipeline Result.

Standard return object for Intelligence Pipeline execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(slots=True)
class PipelineResult:
    """
    Represents the outcome of a pipeline execution.
    """

    success: bool
    stage: str
    message: str = ""
    context: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the pipeline result.
        """

        return {
            "success": self.success,
            "stage": self.stage,
            "message": self.message,
            "context": self.context,
            "metadata": self.metadata,
        }

    @classmethod
    def success_result(
        cls,
        stage: str,
        context: Dict[str, Any],
        message: str = "",
        metadata: Dict[str, Any] | None = None,
    ) -> "PipelineResult":
        """
        Create a successful pipeline result.
        """

        return cls(
            success=True,
            stage=stage,
            message=message,
            context=context,
            metadata=metadata or {},
        )

    @classmethod
    def failure_result(
        cls,
        stage: str,
        message: str,
        context: Dict[str, Any] | None = None,
        metadata: Dict[str, Any] | None = None,
    ) -> "PipelineResult":
        """
        Create a failed pipeline result.
        """

        return cls(
            success=False,
            stage=stage,
            message=message,
            context=context or {},
            metadata=metadata or {},
        )