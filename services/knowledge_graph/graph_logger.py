from datetime import datetime


class GraphLogger:

    """
    Knowledge Graph logging component.

    Tracks:
    - entity operations
    - relationship operations
    - graph events
    """


    def __init__(self):

        self.logs = []



    def log(
        self,
        event,
        metadata=None
    ):

        if metadata is None:
            metadata = {}


        entry = {

            "event": event,

            "metadata": metadata,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.logs.append(
            entry
        )


        return entry



    def get_logs(
        self
    ):

        return self.logs