from datetime import datetime

from .investigation_context import InvestigationContext
from .engine_router import EngineRouter
from .investigation_pipeline import InvestigationPipeline
from .workflow_controller import WorkflowController
from .decision_tracker import DecisionTracker
from .orchestrator_memory import OrchestratorMemory
from .orchestrator_logger import OrchestratorLogger



class InvestigationOrchestrator:


    def __init__(self):

        self.context = InvestigationContext()

        self.router = EngineRouter()

        self.pipeline = InvestigationPipeline()

        self.workflow = WorkflowController()

        self.decisions = DecisionTracker()

        self.memory = OrchestratorMemory()

        self.logger = OrchestratorLogger()



    def investigate(self, event):


        context = self.context.create(
            event
        )


        engines = self.router.route(
            event
        )


        pipeline = self.pipeline.execute(
            event
        )


        workflow = self.workflow.control(
            event
        )


        decision = self.decisions.track(
            "Security investigation completed"
        )


        memory = self.memory.store(
            event
        )


        log = self.logger.log(
            event
        )


        return {


            "status":
                "completed",


            "investigation_context":
                context,


            "engine_execution":
                engines,


            "pipeline":
                pipeline,


            "workflow":
                workflow,


            "decision":
                decision,


            "memory":
                memory,


            "log":
                log,


            "created_at":
                datetime.utcnow().isoformat()

        }