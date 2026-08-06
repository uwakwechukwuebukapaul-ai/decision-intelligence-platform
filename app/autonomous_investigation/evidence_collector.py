"""
Sentinel DNA Evidence Collector

Collects available intelligence evidence.
"""


class EvidenceCollector:


    def collect(
        self,
        intelligence: dict,
    ):


        return {


            "evidence":

                {


                    "risk":

                        intelligence.get(
                            "risk",
                            {},
                        ),


                    "reputation":

                        intelligence.get(
                            "reputation",
                            {}),


                    "threat_context":

                        intelligence.get(
                            "threat_context",
                            {}),


                    "mitre_mapping":

                        intelligence.get(
                            "mitre_mapping",
                            []),

                },


            "collection_status":

                "completed",

        }