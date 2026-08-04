from datetime import datetime, timezone


class ResponseLogger:


    def log(self, data):

        return {
            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "logged": True,

            "data": data
        }