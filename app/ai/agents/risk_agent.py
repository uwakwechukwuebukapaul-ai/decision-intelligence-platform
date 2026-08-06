"""
Sentinel DNA Risk Analysis Agent

Calculates investigation risk.
"""


from .base_agent import BaseAgent



class RiskAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "RiskAgent"
        )


    def analyze(
        self,
        investigation
    ):


        evidence_score = (
            len(investigation.evidence) * 10
        )


        finding_score = (
            len(investigation.state.findings) * 5
        )


        total_score = (
            evidence_score +
            finding_score
        )


        investigation.state.set_risk_score(
            total_score
        )


        result = {

            "agent":
                self.name,

            "risk_score":
                total_score,

            "severity":
                self.calculate_severity(
                    total_score
                )

        }


        investigation.add_finding(
            f"Risk calculated: {total_score}"
        )


        return result



    def calculate_severity(
        self,
        score
    ):


        if score >= 70:
            return "CRITICAL"

        if score >= 40:
            return "HIGH"

        if score >= 20:
            return "MEDIUM"

        return "LOW"