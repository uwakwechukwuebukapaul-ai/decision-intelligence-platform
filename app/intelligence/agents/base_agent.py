"""
Base Intelligence Agent

Abstract foundation for all
autonomous intelligence agents.
"""


from .agent_metadata import AgentMetadata



class BaseAgent:


    def __init__(
        self,
        name: str,
        version: str,
        capabilities: list[str],
    ):

        self.metadata = AgentMetadata(
            name,
            version,
            capabilities,
        )


    def execute(
        self,
        payload: dict,
    ):

        raise NotImplementedError(
            "Agent execution must be implemented"
        )


    def health_check(self):

        return {

            "agent":
                self.metadata.name,

            "status":
                self.metadata.status

        }


    def get_metadata(self):

        return self.metadata.to_dict()