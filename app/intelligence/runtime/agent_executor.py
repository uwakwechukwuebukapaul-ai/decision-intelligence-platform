"""
Agent Executor

Connects runtime execution
with registered intelligence agents.
"""


class AgentExecutor:

    def __init__(
        self,
        agent_registry,
    ):

        self.agent_registry = agent_registry


    def execute(
        self,
        job,
    ):

        job.start()

        agent = self._resolve_agent(
            job.capability
        )


        if agent is None:

            job.fail()

            return {

                "status":
                    "failed",

                "reason":
                    f"No agent found for capability: {job.capability}"

            }


        try:

            result = agent.execute(
                job.payload
            )


            job.complete()


            return {

                "status":
                    "completed",

                "agent":
                    agent.metadata.name,

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


    def _resolve_agent(
        self,
        capability,
    ):

        for agent in self.agent_registry.agents.values():

            if capability in agent.metadata.capabilities:

                return agent


        return None