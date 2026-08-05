class CampaignTracker:
    """
    Tracks threat campaigns and adversary activity.
    """

    def __init__(self):
        self.name = "Campaign Tracker"


    def track(self, campaign):

        return {
            "campaign": campaign,
            "status": "tracking",
            "actors": []
        }


    def history(self):

        return []