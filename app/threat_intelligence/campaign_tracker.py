from datetime import datetime


class CampaignTracker:
    """
    Tracks threat campaigns.
    """


    def track(
        self,
        event
    ):

        return {

            "campaign":
                "Unknown Threat Campaign",

            "event":
                event,

            "status":
                "MONITORING",

            "timestamp":
                datetime.utcnow().isoformat()

        }