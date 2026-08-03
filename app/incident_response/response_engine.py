from datetime import datetime

from .incident_manager import IncidentManager
from .containment_engine import ContainmentEngine
from .eradication_engine import EradicationEngine
from .recovery_manager import RecoveryManager
from .forensics_engine import ForensicsEngine
from .communication_manager import CommunicationManager
from .response_memory import ResponseMemory
from .response_logger import ResponseLogger


class IncidentResponseEngine:

    def __init__(self):

        self.incident_manager = IncidentManager()
        self.containment = ContainmentEngine()
        self.eradication = EradicationEngine()
        self.recovery = RecoveryManager()
        self.forensics = ForensicsEngine()
        self.communication = CommunicationManager()
        self.memory = ResponseMemory()
        self.logger = ResponseLogger()


    def respond(self, incident):

        incident_data = self.incident_manager.create_incident(
            incident
        )

        containment = self.containment.contain(
            incident
        )

        eradication = self.eradication.eradicate(
            incident
        )

        recovery = self.recovery.recover(
            incident
        )

        forensics = self.forensics.analyze(
            incident
        )

        communication = self.communication.notify(
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

            "incident_record": incident_data,

            "containment": containment,

            "eradication": eradication,

            "recovery": recovery,

            "forensics": forensics,

            "communication": communication,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }