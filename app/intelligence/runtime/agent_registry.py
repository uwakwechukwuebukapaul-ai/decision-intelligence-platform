"""
Agent Registry

Registers Sentinel DNA intelligence capabilities.
"""


class AgentRegistry:
    """
    Registry builder for intelligence engines.
    """

    def __init__(self, registry):
        self.registry = registry


    def register_engine(
        self,
        capability,
        engine,
    ):
        self.registry.register(
            capability,
            engine,
        )


    def register_all(
        self,
        engines,
    ):
        for capability, engine in engines.items():

            self.register_engine(
                capability,
                engine,
            )

        return self.registry