"""
Sentinel DNA Threat Intelligence Agent

Analyzes investigation evidence
for threat intelligence indicators.
"""


from .base_agent import BaseAgent



class ThreatIntelligenceAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "ThreatIntelligenceAgent"
        )


    def analyze(
        self,
        investigation
    ):

        findings = []

        indicators = investigation.evidence


        if indicators:

            findings.append(
                f"Enriched {len(indicators)} indicators"
            )

        else:

            findings.append(
                "No indicators available"
            )


        result = {

            "agent":
                self.name,

            "findings":
                findings,

            "intel_score":
                len(indicators) * 15

        }


        for finding in findings:

            investigation.add_finding(
                finding
            )


        return result