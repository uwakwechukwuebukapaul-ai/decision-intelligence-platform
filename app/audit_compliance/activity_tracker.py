from datetime import datetime


class ActivityTracker:
    """
    Tracks analyst and system activities.
    """


    def track(
        self,
        user,
        action,
        resource
    ):

        return {

            "user":
                user,

            "action":
                action,

            "resource":
                resource,

            "timestamp":
                datetime.utcnow().isoformat(),

            "status":
                "logged"

        }