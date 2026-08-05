from datetime import datetime
import uuid


class InvestigationSession:
    """
    Represents a single autonomous SOC investigation.
    """


    def __init__(
        self,
        event
    ):

        self.session_id = (
            "INV-"
            + str(uuid.uuid4())[:8]
        )

        self.event = event

        self.status = "initialized"

        self.created = datetime.utcnow().isoformat()

        self.actions = []

        self.findings = []



    def add_action(
        self,
        action
    ):

        self.actions.append(action)



    def add_finding(
        self,
        finding
    ):

        self.findings.append(finding)



    def complete(self):

        self.status = "completed"



    def to_dict(self):

        return {

            "session_id": self.session_id,

            "event": self.event,

            "status": self.status,

            "actions": self.actions,

            "findings": self.findings,

            "created": self.created

        }