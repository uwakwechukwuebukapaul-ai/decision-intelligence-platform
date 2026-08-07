"""
Sentinel DNA
Intelligence Runtime Executor

Executes registered intelligence engines safely.
"""

import inspect


class IntelligenceExecutor:

    def __init__(
        self,
        registry,
    ):

        self.registry = registry


    def execute(
        self,
        job,
    ):

        handler = self.registry.resolve(
            job.capability
        )


        if handler is None:

            raise ValueError(
                f"Unknown capability: {job.capability}"
            )


        try:

            execute_method = handler.execute


            parameters = inspect.signature(
                execute_method
            ).parameters


            # execute(payload)
            if len(parameters) == 1:

                result = execute_method(
                    job.payload
                )


            # execute(payload, context)
            else:

                result = execute_method(
                    job.payload,
                    job.context
                )


            return {

                "status":
                    "completed",

                "capability":
                    job.capability,

                "result":
                    result,

            }


        except Exception as error:


            return {

                "status":
                    "failed",

                "capability":
                    job.capability,

                "error":
                    str(error),

            }