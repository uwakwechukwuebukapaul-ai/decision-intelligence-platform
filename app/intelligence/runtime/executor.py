"""
Intelligence Runtime Executor
"""



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

            result = handler.execute(
                job.payload,
                job.context,
            )


            return {

                "status": "completed",

                "capability": job.capability,

                "result": result,

            }


        except TypeError:

            # backward compatibility
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