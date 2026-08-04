from datetime import datetime, timezone


class CoreLogger:


    def log(self, data):

        return {

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "logged":
                True,

            "component":
                "sentinel_core",

            "data":
                data
        }