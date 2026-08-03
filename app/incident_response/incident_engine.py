from datetime import datetime

from .case_manager import CaseManager
from .evidence_manager import EvidenceManager
from .timeline_engine import TimelineEngine
from .analyst_workflow import AnalystWorkflow
from .severity_engine import SeverityEngine
from .report_generator import ReportGenerator


class IncidentEngine:


    def __init__(self):

        self.cases = CaseManager()
        self.evidence = EvidenceManager()
        self.timeline = TimelineEngine()
        self.workflow = AnalystWorkflow()
        self.severity = SeverityEngine()
        self.report = ReportGenerator()



    def create_incident(self, alert):


        severity = self.severity.calculate(alert)


        case = self.cases.create_case(
            alert,
            severity
        )


        evidence = self.evidence.collect(alert)


        timeline = self.timeline.build(
            alert
        )


        workflow = self.workflow.assign(
            case
        )


        report = self.report.generate(
            case,
            evidence,
            timeline
        )


        return {

            "status": "completed",

            "incident": case,

            "severity": severity,

            "evidence": evidence,

            "timeline": timeline,

            "workflow": workflow,

            "report": report,

            "created_at":
                datetime.utcnow().isoformat()

        }