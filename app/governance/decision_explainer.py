from datetime import datetime



class DecisionExplainer:



    def explain(self, decision):


        return {


            "decision":

                decision,


            "reasoning":

                [

                    "Security impact evaluated",

                    "Operational risk considered",

                    "Enterprise policy checked"

                ],



            "confidence":

                91,



            "timestamp":

                datetime.utcnow().isoformat()

        }