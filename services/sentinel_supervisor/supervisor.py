from .decision_engine import DecisionEngine
from .agent_selector import AgentSelector
from .execution_monitor import ExecutionMonitor


class SentinelSupervisor:
    """
    Autonomous SOC command layer.

    Coordinates:
    - decision making
    - agent selection
    - execution tracking
    """


    def __init__(self):

        self.decision_engine = DecisionEngine()

        self.agent_selector = AgentSelector()

        self.monitor = ExecutionMonitor()



    def investigate(
        self,
        incident
    ):

        decision = (
            self.decision_engine
            .evaluate(incident)
        )


        agents = (
            self.agent_selector
            .select(incident)
        )


        return {

            "incident": incident,

            "decision": decision,

            "assigned_agents": agents,

            "status":
            "supervisor_workflow_created"
        }



    def record_execution(
        self,
        agent,
        action,
        status
    ):

        return (
            self.monitor.record(
                agent,
                action,
                status
            )
        )