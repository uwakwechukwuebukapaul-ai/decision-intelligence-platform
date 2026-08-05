from .incident import Incident
from .severity_engine import SeverityEngine
from .assignment_engine import AssignmentEngine
from .timeline_manager import TimelineManager



class IncidentManager:
    """
    Central SOC incident lifecycle controller.
    """


    def __init__(self):

        self.incidents = {}

        self.severity = SeverityEngine()

        self.assignment = AssignmentEngine()

        self.timeline = TimelineManager()



    def create(
        self,
        title,
        description,
        source="engine"
    ):


        incident = Incident(

            title,

            description,

            source

        )


        incident.severity = (

            self.severity.calculate(
                description
            )

        )


        incident.assign(

            self.assignment.assign()

        )


        incident.update_status(
            "investigating"
        )


        self.timeline.add(

            incident,

            "Incident created"

        )


        self.incidents[incident.id] = incident


        return incident



    def get(
        self,
        incident_id
    ):

        incident = self.incidents.get(
            incident_id
        )


        if incident:

            return incident.to_dict()


        return None



    def list_all(
        self
    ):

        return [

            incident.to_dict()

            for incident in self.incidents.values()

        ]