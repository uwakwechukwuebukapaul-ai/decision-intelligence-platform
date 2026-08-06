"""
Intelligence Executor

Executes intelligence jobs
through capability routing.
"""

from .capability_router import CapabilityRouter


class IntelligenceExecutor:

    def __init__(
        self,
        router: CapabilityRouter | None = None,
    ):

        self.router = (
            router
            or CapabilityRouter()
        )


    def register_capability(
        self,
        capability: str,
        handler,
    ):

        self.router.register(
            capability,
            handler
        )


    def execute(
        self,
        job,
    ):

        job.start()

        handler = self.router.resolve(
            job.capability
        )


        if handler is None:

            job.fail()

            return {
                "status": "failed",
                "reason":
                    f"No handler registered for {job.capability}"
            }


        try:

            result = handler(
                job.payload
            )

            job.complete()

            return {

                "status":
                    "completed",

                "job":
                    job.to_dict(),

                "result":
                    result
            }


        except Exception as error:

            job.fail()

            return {

                "status":
                    "failed",

                "error":
                    str(error),

                "job":
                    job.to_dict()
            }