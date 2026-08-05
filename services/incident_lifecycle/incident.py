from datetime import datetime
import uuid


class Incident:
    """
    Sentinel DNA incident object.

    Represents a complete SOC case lifecycle.
    """


    def __init__(
        self,
        title,
        description,
        source="unknown"
    ):

        self.id = (
            "INC-"
            + datetime.utcnow().strftime("%Y%m%d")
            + "-"
            + str(uuid.uuid4())[:8]
        )


        self.title = title

        self.description = description

        self.source = source

        self.status = "new"

        self.severity = "unknown"

        self.owner = None

        self.timeline = []


    def update_status(
        self,
        status
    ):

        self.status = status


    def assign(
        self,
        analyst
    ):

        self.owner = analyst


    def add_event(
        self,
        event
    ):

        self.timeline.append(

            {
                "event": event,

                "timestamp":
                datetime.utcnow().isoformat()

            }

        )


    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "description": self.description,

            "source": self.source,

            "status": self.status,

            "severity": self.severity,

            "owner": self.owner,

            "timeline": self.timeline

        }