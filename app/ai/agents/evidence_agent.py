"""
Sentinel DNA Evidence Investigation Agent

First SOC analysis agent.

Analyzes investigation evidence
and produces findings.
"""


from .base_agent import BaseAgent



class EvidenceAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "EvidenceAgent"
        )



    def analyze(
        self,
        investigation
    ):


        findings = []


        evidence = investigation.evidence


        if not evidence:

            findings.append(
                "No evidence available"
            )


        else:

            findings.append(
                f"Analyzed {len(evidence)} evidence items"
            )



        result = {

            "agent":
                self.name,

            "findings":
                findings,

            "risk_score":
                len(evidence) * 10

        }



        for finding in findings:

            investigation.add_finding(
                finding
            )


        investigation.state.set_risk_score(
            result["risk_score"]
        )


        return result