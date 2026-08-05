from .workflow_manager import WorkflowManager
from .decision_router import DecisionRouter
from .agent_scheduler import AgentScheduler
from .execution_controller import ExecutionController


class AutonomousOrchestrator:
    """
    Sentinel DNA Autonomous SOC Orchestrator.

    Coordinates intelligence engines,
    investigation workflows and response execution.
    """

    def __init__(self):

        self.workflow = WorkflowManager()
        self.router = DecisionRouter()
        self.scheduler = AgentScheduler()
        self.executor = ExecutionController()


    def orchestrate(self, event):

        decision = self.router.route(event)

        workflow = self.workflow.create_workflow(
            event,
            decision
        )

        agents = self.scheduler.schedule(
            workflow
        )

        execution = self.executor.execute(
            workflow,
            agents
        )

        return {

            "event": event,

            "decision":
                decision,

            "workflow":
                workflow,

            "agents":
                agents,

            "execution":
                execution,

            "status":
                "orchestration_completed"

        }