"""
Sentinel DNA - Campaign Intelligence Store

Stores detected threat campaigns.

Future expansion:
- Database persistence
- Graph database backend
- Threat intelligence feeds
"""


class CampaignStore:


    def __init__(self):

        self.campaigns = []



    def save(
        self,
        campaign: dict,
    ):

        self.campaigns.append(
            campaign
        )

        return campaign



    def list_all(self):

        return self.campaigns



    def find_by_indicator(
        self,
        indicator: str,
    ):

        results = []


        for campaign in self.campaigns:

            if indicator in campaign.get(
                "indicators",
                []
            ):

                results.append(
                    campaign
                )


        return results