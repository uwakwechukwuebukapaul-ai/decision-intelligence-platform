from datetime import datetime


class ScenarioGenerator:

    def __init__(self):
        self.version = "1.0"


    def generate(self, user_id):

        return {

            "user_id": user_id,

            "scenario_status": "generated",

            "scenarios": [

                {
                    "scenario_id": "SCN-001",
                    "name": "Optimistic Outcome",
                    "description":
                        "Decision produces maximum positive results",
                    "risk": "low"
                },

                {
                    "scenario_id": "SCN-002",
                    "name": "Balanced Outcome",
                    "description":
                        "Decision produces expected results",
                    "risk": "medium"
                },

                {
                    "scenario_id": "SCN-003",
                    "name": "Adverse Outcome",
                    "description":
                        "Decision produces unexpected negative impact",
                    "risk": "high"
                }

            ],

            "generated_at":
                datetime.utcnow().isoformat(),

            "version": self.version
        }