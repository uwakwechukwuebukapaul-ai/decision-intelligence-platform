"""
Investigation Assessor

Produces SOC analyst conclusions.
"""


class InvestigationAssessor:


    def assess(
        self,
        signals,
    ):

        risk_score = signals.get(
            "risk_score",
            0,
        )


        classification = signals.get(
            "classification",
            "unknown",
        )


        reasons = []


        if risk_score >= 70:

            reasons.append(
                "High risk score detected"
            )


        if classification == "malicious":

            reasons.append(
                "Malicious activity classified"
            )


        verdict = (
            "malicious"
            if reasons
            else "benign"
        )


        confidence = (
            0.90
            if verdict == "malicious"
            else 0.50
        )


        return {

            "verdict": verdict,

            "confidence": confidence,

            "reasoning": reasons,

        }