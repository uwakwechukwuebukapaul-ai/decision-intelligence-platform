from datetime import datetime


class InvestigationPipeline:


    def run(self, alert, intelligence):

        return {

            "incident": alert,

            "steps": [

                "Collect evidence",

                "Analyze indicators",

                "Map attack techniques",

                "Assess risk",

                "Generate response plan"

            ],

            "intelligence_used": intelligence["sources"],

            "status": "investigation_completed",

            "timestamp": datetime.utcnow().isoformat()

        }