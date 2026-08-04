from datetime import datetime, timezone


class GraphLogger:


    def log(self, message):

        return {

            "message": message,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }