from datetime import datetime

from .containment_manager import ContainmentManager
from .eradication_engine import EradicationEngine
from .recovery_manager import RecoveryManager
from .forensics_engine import ForensicsEngine
from .timeline_reconstructor import TimelineReconstructor
from .incident_reporter import IncidentReporter
from .lessons_learned import LessonsLearned
from .response_memory import ResponseMemory


class IncidentResponseEngine:

    def __init__(self):
        self.forensics = ForensicsEngine()
        self.containment = ContainmentManager()
        self.eradication = EradicationEngine()
        self.recovery = RecoveryManager()
        self.timeline = TimelineReconstructor()
        self.reporter = IncidentReporter()
        self.lessons = LessonsLearned()
        self.memory = ResponseMemory()

    def respond(self, incident):

        forensic_result = self.forensics.collect(incident)

        containment_result = self.containment.contain(incident)

        eradication_result = self.eradication.remove(incident)

        recovery_result = self.recovery.restore(incident)

        timeline_result = self.timeline.reconstruct(incident)

        report_result = self.reporter.generate(
            incident,
            forensic_result,
            containment_result,
            recovery_result
        )

        lessons_result = self.lessons.analyze(incident)

        self.memory.store(incident)

        return {
            "status": "completed",
            "incident": incident,
            "forensics": forensic_result,
            "containment": containment_result,
            "eradication": eradication_result,
            "recovery": recovery_result,
            "timeline": timeline_result,
            "report": report_result,
            "lessons_learned": lessons_result,
            "created_at": datetime.utcnow().isoformat()
        }