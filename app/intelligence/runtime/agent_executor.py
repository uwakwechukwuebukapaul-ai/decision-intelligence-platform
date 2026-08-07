"""
Sentinel DNA - Agent Executor

Executes registered intelligence agents.
"""


class AgentExecutor:

    def __init__(
        self,
        registry,
    ):

        self.registry = registry


    def execute(
        self,
        job,
    ):

        try:

            agent = None


            for registered_agent in self.registry.agents.values():

                capabilities = (
                    registered_agent.metadata.capabilities
                )


                if job.capability in capabilities:

                    agent = registered_agent
                    break



            if agent is None:

                raise Exception(
                    "Agent not found"
                )


            # Update lifecycle
            job.start()


            result = agent.execute(
                job.payload
            )


            # Mark successful execution
            job.complete(
                result
            )


            return {

                "status":
                    "completed",

                "agent":
                    agent.metadata.name,

                "result":
                    result,

            }



        except Exception as error:


            # Mark failed execution
            job.fail(
                error
            )


            return {

                "status":
                    "failed",

                "error":
                    str(error),

            }