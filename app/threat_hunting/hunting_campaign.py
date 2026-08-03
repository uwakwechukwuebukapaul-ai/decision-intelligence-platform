from datetime import datetime
import uuid


class HuntingCampaign:

    def create(self, threat):

        return {
            "campaign_id":
                f"HUNT-{uuid.uuid4().hex[:8].upper()}",
            "name":
                "Autonomous Threat Hunt",
            "target":
                threat,
            "status":
                "ACTIVE",
            "created_at":
                datetime.utcnow().isoformat()
        }