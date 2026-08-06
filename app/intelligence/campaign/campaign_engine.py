"""
Sentinel DNA - Campaign Intelligence Engine

Transforms correlated intelligence
into threat campaign intelligence.
"""


from datetime import datetime

from .campaign_detector import CampaignDetector

from .campaign_schema import CampaignResult

from .campaign_store import CampaignStore





class CampaignEngine:


    def __init__(self):

        self.detector = CampaignDetector()

        self.store = CampaignStore()



    def analyze(
        self,
        intelligence_items: list[dict],
    ):


        detection = self.detector.detect(
            intelligence_items
        )



        campaign = CampaignResult(

            campaign_id=
            f"CAMP-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",


            indicators=
            detection["indicators"],


            confidence=
            detection["confidence"],


            techniques=
            detection["techniques"],


            reasoning=
            detection["reasoning"],

        )



        result = {

            "campaign_id":
            campaign.campaign_id,


            "campaign_detected":
            detection["campaign_detected"],


            "confidence":
            campaign.confidence,


            "indicators":
            campaign.indicators,


            "techniques":
            campaign.techniques,


            "reasoning":
            campaign.reasoning,


            "created_at":
            campaign.created_at,

        }



        return self.store.save(
            result
        )