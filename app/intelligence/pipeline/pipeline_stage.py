"""
Base Pipeline Stage.

Defines the interface implemented by every stage in the
Intelligence Execution Pipeline.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class PipelineStage(ABC):
    """
    Abstract base class for all pipeline stages.
    """

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        """
        Human-readable stage name.
        """
        return self._name

    @abstractmethod
    def execute(
        self,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Execute this stage.

        Parameters
        ----------
        context:
            Shared execution context.

        Returns
        -------
        dict
            Updated execution context.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"