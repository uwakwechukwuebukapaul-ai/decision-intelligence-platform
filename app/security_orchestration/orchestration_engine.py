from datetime import datetime

from .event_processor import EventProcessor
from .security_pipeline import SecurityPipeline
from .engine_connector import EngineConnector
from .decision_manager import DecisionManager
from .response_manager import ResponseManager
from .orchestration_memory import OrchestrationMemory
from .orchestration_logger import OrchestrationLogger


class SecurityOrchestrationEngine:

    def __init__(self):

        self.processor = EventProcessor()
        self.pipeline = SecurityPipeline()
        self.connector = EngineConnector()
        self.decision = DecisionManager()
        self.response = ResponseManager()
        self.memory = OrchestrationMemory()
        self.logger = OrchestrationLogger()


    def orchestrate(self, event):

        processed = self.processor.process(event)

        pipeline = self.pipeline.execute(event)

        engines = self.connector.connect(event)

        decision = self.decision.decide(event)

        response = self.response.prepare(event)

        memory = self.memory.store(event)

        log = self.logger.log(event)


        return {

            "status": "completed",

            "event": event,

            "processed_event": processed,

            "pipeline": pipeline,

            "engines": engines,

            "decision": decision,

            "response": response,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }