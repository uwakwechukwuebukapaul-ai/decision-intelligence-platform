"""
Agent Lifecycle Manager

Controls the operational state of
registered intelligence agents.
"""


class AgentLifecycle:

    VALID_STATES = {
        "active",
        "paused",
        "stopped",
    }

    def __init__(self):

        self._states = {}

    def register(self, agent):

        self._states[agent.metadata.name] = "active"

    def start(self, agent):

        self._states[agent.metadata.name] = "active"
        agent.metadata.activate()

    def pause(self, agent):

        self._states[agent.metadata.name] = "paused"
        agent.metadata.status = "paused"

    def stop(self, agent):

        self._states[agent.metadata.name] = "stopped"
        agent.metadata.deactivate()

    def resume(self, agent):

        self.start(agent)

    def state(self, agent):

        return self._states.get(
            agent.metadata.name,
            "unknown",
        )