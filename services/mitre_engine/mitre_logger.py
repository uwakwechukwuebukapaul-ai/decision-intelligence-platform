from datetime import datetime, timezone



class MitreLogger:



    def log(self, message):

        return {

            "message": message,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }