from datetime import datetime

from .incident_classifier import IncidentClassifier
from .containment_planner import ContainmentPlanner
from .eradication_planner import EradicationPlanner
from .recovery_planner import RecoveryPlanner
from .response_coordinator import ResponseCoordinator
from .lessons_learned import LessonsLearned
from .response_memory import ResponseMemory
from .response_logger import ResponseLogger


class IncidentResponseEngine:


    def __init__(self):

        self.classifier = IncidentClassifier()
        self.containment = ContainmentPlanner()
        self.eradication = EradicationPlanner()
        self.recovery = RecoveryPlanner()
        self.coordinator = ResponseCoordinator()
        self.lessons = LessonsLearned()
        self.memory = ResponseMemory()
        self.logger = ResponseLogger()


    def respond(self, incident):

        classification = self.classifier.classify(
            incident
        )

        containment = self.containment.plan(
            incident
        )

        eradication = self.eradication.plan(
            incident
        )

        recovery = self.recovery.plan(
            incident
        )

        coordination = self.coordinator.coordinate(
            incident
        )

        lessons = self.lessons.generate(
            incident
        )

        memory = self.memory.store(
            incident
        )

        log = self.logger.record(
            incident
        )


        return {

            "status": "completed",

            "incident": incident,

            "classification": classification,

            "containment": containment,

            "eradication": eradication,

            "recovery": recovery,

            "coordination": coordination,

            "lessons_learned": lessons,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()
        }