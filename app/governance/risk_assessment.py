from datetime import datetime



class RiskAssessment:



    def assess(self, action):


        high_risk_keywords = [

            "delete",

            "isolate",

            "disable",

            "block",

            "terminate"

        ]



        risk = "low"



        for keyword in high_risk_keywords:

            if keyword in action.lower():

                risk = "high"



        return {


            "risk_level":

                risk,


            "risk_categories":

                [

                    "Security Risk",

                    "Operational Risk",

                    "Business Risk"

                ],



            "timestamp":

                datetime.utcnow().isoformat()

        }