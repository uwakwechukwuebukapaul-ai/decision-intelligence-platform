from datetime import datetime

from .activity_tracker import ActivityTracker
from .compliance_mapper import ComplianceMapper
from .policy_engine import PolicyEngine
from .control_manager import ControlManager
from .audit_storage import AuditStorage
from .compliance_reporter import ComplianceReporter
from .audit_memory import AuditMemory



class AuditEngine:
    """
    Sentinel DNA Enterprise Audit Engine.
    """


    def __init__(self):

        self.activity = ActivityTracker()

        self.mapper = ComplianceMapper()

        self.policy = PolicyEngine()

        self.controls = ControlManager()

        self.storage = AuditStorage()

        self.reporter = ComplianceReporter()

        self.memory = AuditMemory()



    def record(
        self,
        user,
        action,
        resource
    ):


        activity = self.activity.track(
            user,
            action,
            resource
        )


        compliance = self.mapper.map_control(
            action
        )


        stored = self.storage.save(
            activity
        )


        self.memory.store(
            activity
        )


        return {


            "status":
                "completed",


            "activity":
                activity,


            "compliance":
                compliance,


            "storage":
                stored,


            "created_at":
                datetime.utcnow().isoformat()

        }



    def generate_report(self):

        history = self.memory.history()

        return self.reporter.generate(
            history["events"]
        )