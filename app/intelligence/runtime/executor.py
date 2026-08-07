"""
Intelligence Runtime Executor

Executes intelligence jobs through
registered capabilities.
"""

from .registry import CapabilityRegistry


class IntelligenceExecutor:
    """
    Executes IntelligenceJob objects.
    """

    def __init__(
        self,
        registry: CapabilityRegistry,
    ):
        self.registry = registry


    def execute(
        self,
        job,
    ):
        """
        Execute intelligence job.
        """

        handler = self.registry.resolve(
            job.capability
        )


        if handler is None:
            raise ValueError(
                f"Unknown capability: {job.capability}"
            )


        try:

            result = handler.execute(
                job.payload
            )


            return {
                "status": "completed",
                "capability": job.capability,
                "result": result,
            }


        except Exception as error:

            return {
                "status": "failed",
                "capability": job.capability,
                "error": str(error),
            }