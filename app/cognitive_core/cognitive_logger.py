import datetime
import uuid


class CognitiveLogger:
    """
    Cognitive engine execution logger.
    """


    def log(self, event):

        return {

            "log_id":
                "COGLOG-"
                + uuid.uuid4()
                .hex[:8]
                .upper(),

            "event":
                "Cognitive investigation executed",

            "data":
                event,

            "timestamp":
                datetime.datetime.utcnow().isoformat()

        }