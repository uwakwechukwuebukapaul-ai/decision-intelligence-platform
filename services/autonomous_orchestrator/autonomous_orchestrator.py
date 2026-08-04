import datetime

from .investigation_controller import InvestigationController
from .engine_coordinator import EngineCoordinator
from .decision_pipeline import DecisionPipeline
from .response_coordinator import ResponseCoordinator
from .orchestrator_memory import OrchestratorMemory
from .orchestrator_logger import OrchestratorLogger


class AutonomousOrchestrator:

    def __init__(self):
        self.investigation = InvestigationController()
        self.engine = EngineCoordinator()
        self.decision = DecisionPipeline()
        self.response = ResponseCoordinator()
        self.memory = OrchestratorMemory()
        self.logger = OrchestratorLogger()


    def orchestrate(self, event):

        investigation = self.investigation.control(event)

        engines = self.engine.coordinate(event)

        decision = self.decision.evaluate(
            investigation,
            engines
        )

        response = self.response.execute(decision)

        memory = self.memory.store(
            event,
            decision,
            response
        )

        log = self.logger.log(event)


        return {
            "status": "completed",
            "event": event,
            "investigation": investigation,
            "engines": engines,
            "decision": decision,
            "response": response,
            "memory": memory,
            "log": log,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
