from datetime import datetime

from .alert_processor import AlertProcessor
from .investigation_pipeline import InvestigationPipeline
from .intelligence_router import IntelligenceRouter
from .copilot_engine import CopilotEngine
from .workflow_manager import WorkflowManager
from .platform_memory import PlatformMemory
from .platform_logger import PlatformLogger


class AISOCPlatformEngine:

    def __init__(self):

        self.alert_processor = AlertProcessor()
        self.pipeline = InvestigationPipeline()
        self.router = IntelligenceRouter()
        self.copilot = CopilotEngine()
        self.workflow = WorkflowManager()
        self.memory = PlatformMemory()
        self.logger = PlatformLogger()


    def investigate(self, alert):

        processed_alert = self.alert_processor.process(alert)

        intelligence = self.router.collect(
            alert,
            processed_alert
        )

        investigation = self.pipeline.run(
            alert,
            intelligence
        )

        copilot = self.copilot.analyze(
            alert,
            investigation
        )

        workflow = self.workflow.execute(
            alert,
            copilot
        )

        memory = self.memory.store(
            alert,
            investigation
        )

        log = self.logger.record(
            alert,
            workflow
        )


        return {

            "status": "completed",

            "alert": alert,

            "processed_alert": processed_alert,

            "intelligence": intelligence,

            "investigation": investigation,

            "copilot": copilot,

            "workflow": workflow,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }