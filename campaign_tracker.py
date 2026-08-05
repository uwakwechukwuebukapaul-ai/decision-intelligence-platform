class CampaignTracker:

    def track(self, campaign):

        return {
            "campaign": campaign,
            "status": "tracking",
            "actors": []
        }

    def history(self):

        return []