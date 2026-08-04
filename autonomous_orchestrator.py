from datetime import datetime, timezone

from .investigation_controller import InvestigationController
from .engine_coordinator import EngineCoordinator
from .decision_pipeline import DecisionPipeline
from .response_coordinator import ResponseCoordinator
from .orchestrator_memory import OrchestratorMemory
from .orchestrator_logger import OrchestratorLogger



class AutonomousOrchestrator:


    def __init__(self):

        self.investigation_controller = InvestigationController()

        self.engine_coordinator = EngineCoordinator()

        self.decision_pipeline = DecisionPipeline()

        self.response_coordinator = ResponseCoordinator()

        self.memory = OrchestratorMemory()

        self.logger = OrchestratorLogger()



    def execute(
        self,
        event
    ):


        investigation = self.investigation_controller.start(
            event
        )


        engines = self.engine_coordinator.coordinate(
            event
        )


        decision = self.decision_pipeline.evaluate(
            investigation,
            engines
        )


        response = self.response_coordinator.prepare(
            decision
        )


        if hasattr(self.memory,"store"):

            memory = self.memory.store(
                event,
                decision
            )

        else:

            memory = self.memory.remember(
                event,
                decision
            )



        log = self.logger.log(
            {
                "event": event,
                "decision": decision
            }
        )


        return {

            "status":
                "completed",

            "event":
                event,

            "investigation":
                investigation,

            "engines":
                engines,

            "decision":
                decision,

            "response":
                response,

            "memory":
                memory,

            "log":
                log,

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }



    def run(
        self,
        event
    ):

        return self.execute(
            event
        )