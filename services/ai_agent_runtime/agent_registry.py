class AgentRegistry:
    """
    Central registry for Sentinel DNA autonomous agents.
    """

    def __init__(self):
        self.registry = {}

    def register(self, name, metadata=None):

        self.registry[name] = metadata or {}

        return {
            "agent": name,
            "registered": True
        }

    def lookup(self, name):
        return self.registry.get(name)

    def all_agents(self):
        return self.registry