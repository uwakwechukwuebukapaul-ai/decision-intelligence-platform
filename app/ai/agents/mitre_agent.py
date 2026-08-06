"""
Sentinel DNA MITRE ATT&CK Agent

Maps investigation activity
to ATT&CK techniques.
"""


from .base_agent import BaseAgent



class MitreAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "MitreAgent"
        )


    def analyze(
        self,
        investigation
    ):


        techniques = []


        for evidence in investigation.evidence:

            if "email" in str(evidence).lower():

                techniques.append(
                    "T1566 - Phishing"
                )


        if not techniques:

            techniques.append(
                "No ATT&CK technique identified"
            )


        result = {

            "agent":
                self.name,

            "techniques":
                techniques

        }


        for technique in techniques:

            investigation.add_finding(
                technique
            )


        return result