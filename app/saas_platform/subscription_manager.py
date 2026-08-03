from datetime import datetime


class SubscriptionManager:

    def create(self, tenant):

        return {
            "tenant": tenant,
            "plan": "Enterprise",
            "features": [
                "AI SOC Analyst",
                "Threat Intelligence",
                "SOAR Automation",
                "MITRE Mapping"
            ],
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }