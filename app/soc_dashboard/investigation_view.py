from datetime import datetime


class InvestigationView:


    def generate(self, incident):

        return {

            "investigation_stage":

            [

                "Evidence Collection",
                "Threat Analysis",
                "Risk Evaluation",
                "Response Decision"

            ],

            "incident":

                incident,

            "timestamp":

                datetime.utcnow().isoformat()
        }