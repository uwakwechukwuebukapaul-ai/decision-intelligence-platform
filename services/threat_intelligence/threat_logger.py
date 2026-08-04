import datetime


class ThreatLogger:

    def log(self, data):

        return {
            "logged_at": datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat(),
            "data": data
        }