"""
Reasoning Engine

Combines intelligence outputs.
"""


from .investigation_assessor import (
    InvestigationAssessor,
)



class ReasoningEngine:


    def __init__(self):

        self.assessor = InvestigationAssessor()



    def analyze(
        self,
        intelligence_results,
    ):

        signals = {}


        for result in intelligence_results:


            capability = result.get(
                "capability"
            )


            data = result.get(
                "result",
                {}
            )


            if capability == "risk_scoring":

                signals.update(data)


            elif capability == "threat_classification":

                signals.update(data)


            elif capability == "mitre_mapping":

                signals["mitre"] = data



        return self.assessor.assess(
            signals
        )