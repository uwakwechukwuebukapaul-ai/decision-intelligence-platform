from datetime import datetime


class RecommendationEngine:


    def generate(self, incident, reasoning):

        return {

            "recommendations": [

                "Investigate affected assets",

                "Collect forensic evidence",

                "Review indicators",

                "Prepare containment"

            ],

            "priority": "critical",

            "timestamp": datetime.utcnow().isoformat()

        }