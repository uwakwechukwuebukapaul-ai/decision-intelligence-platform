from datetime import datetime


class ActionSelector:


    def select(self, incident, recommendations):

        return {

            "actions": [

                "Trigger SOC investigation",

                "Update detection rules",

                "Start threat hunting",

                "Prepare incident response"

            ],

            "execution_mode": "human_approval_required",

            "timestamp": datetime.utcnow().isoformat()

        }