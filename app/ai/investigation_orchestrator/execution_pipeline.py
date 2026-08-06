"""
Sentinel DNA Investigation Execution Pipeline

Responsible for executing AI agents
in a controlled workflow.
"""


class ExecutionPipeline:


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def execute(
        self,
        investigation,
        agents
    ):

        results = []


        for agent_name in agents:

            investigation.state.update_agent(
                agent_name,
                self._running_status()
            )


            result = self.registry.run_agent(
                agent_name,
                investigation
            )


            investigation.state.update_agent(
                agent_name,
                self._completed_status()
            )


            results.append(
                result
            )


        return results



    def _running_status(self):

        from app.investigations import AgentStatus

        return AgentStatus.RUNNING



    def _completed_status(self):

        from app.investigations import AgentStatus

        return AgentStatus.COMPLETED