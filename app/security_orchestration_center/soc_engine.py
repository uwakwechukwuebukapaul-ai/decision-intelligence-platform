from .incident_manager import IncidentManager
from .response_coordinator import ResponseCoordinator
from .soc_repository import SOCRepository
from .soc_schema import create_soc_record


class SOCEngine:

    def __init__(self):

        self.incident_manager = IncidentManager()
        self.response = ResponseCoordinator()
        self.repository = SOCRepository()


    def coordinate(self, event):

        incident = self.incident_manager.create_incident(
            event
        )

        response = self.response.coordinate(
            incident
        )


        workflow = [
            "Incident validated",
            "Threat intelligence correlated",
            "Risk assessment completed",
            "Response actions coordinated"
        ]


        agents = [
            "investigation_agent",
            "threat_agent",
            "response_agent"
        ]


        record = create_soc_record(
            incident["incident_id"],
            incident["priority"],
            workflow,
            agents,
            response["response_status"]
        )


        record["incident"] = incident
        record["response"] = response


        return self.repository.save(record)