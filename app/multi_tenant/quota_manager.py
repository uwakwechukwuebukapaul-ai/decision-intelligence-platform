from datetime import datetime


class QuotaManager:


    def allocate(self, plan):

        quotas = {

            "Enterprise":
                {
                    "users": 500,
                    "events_per_day": 1000000,
                    "cases": "unlimited"
                }

        }


        return {

            "plan":
                plan,

            "quota":
                quotas.get(
                    plan,
                    {}
                ),

            "timestamp":
                datetime.utcnow().isoformat()

        }