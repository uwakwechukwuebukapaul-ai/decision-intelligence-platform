from datetime import datetime


class TimelineManager:
    """
    Maintains investigation history.
    """


    def add(
        self,
        incident,
        action
    ):


        incident.timeline.append(

            {

                "action": action,

                "timestamp":
                datetime.utcnow().isoformat()

            }

        )


        return incident.timeline



    def history(
        self,
        incident
    ):

        return incident.timeline