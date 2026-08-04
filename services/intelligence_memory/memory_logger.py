from datetime import datetime, timezone



class MemoryLogger:


    def log(self, message):

        return {

            "message":
                message,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }