from datetime import datetime


class SubscriptionManager:


    def assign(self, organization):

        return {

            "tenant":
                organization,

            "plan":
                "Enterprise",

            "features":
                [
                    "AI SOC Platform",
                    "Threat Hunting",
                    "Incident Response",
                    "MITRE Intelligence"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }