from datetime import datetime

from .audit_manager import AuditManager
from .evidence_tracker import EvidenceTracker
from .policy_mapper import PolicyMapper
from .framework_mapper import FrameworkMapper
from .control_assessor import ControlAssessor
from .report_generator import ReportGenerator
from .compliance_memory import ComplianceMemory
from .compliance_logger import ComplianceLogger


class ComplianceEngine:

    def __init__(self):

        self.audit = AuditManager()
        self.evidence = EvidenceTracker()
        self.policy = PolicyMapper()
        self.framework = FrameworkMapper()
        self.controls = ControlAssessor()
        self.report = ReportGenerator()
        self.memory = ComplianceMemory()
        self.logger = ComplianceLogger()


    def analyze(self, incident):

        audit = self.audit.create_audit(
            incident
        )

        evidence = self.evidence.track(
            incident
        )

        policy = self.policy.map_policy(
            incident
        )

        frameworks = self.framework.map_frameworks(
            incident
        )

        controls = self.controls.assess(
            incident
        )

        report = self.report.generate(
            incident
        )

        memory = self.memory.store(
            incident
        )

        log = self.logger.log(
            incident
        )


        return {

            "status": "completed",

            "incident": incident,

            "audit": audit,

            "evidence": evidence,

            "policy_mapping": policy,

            "framework_mapping": frameworks,

            "control_assessment": controls,

            "report": report,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }