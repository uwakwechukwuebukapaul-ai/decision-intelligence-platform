"""
Sentinel DNA Executive Summary Generator

Creates management-level incident summaries.
"""


class ExecutiveSummary:


    def generate(
        self,
        investigation
    ):

        risk = investigation.state.risk_score


        severity = self.get_severity(
            risk
        )


        return {

            "incident_id":
                investigation.case_id,

            "investigation_id":
                investigation.investigation_id,

            "severity":
                severity,

            "summary":
                self.create_summary(
                    investigation
                )

        }



    def create_summary(
        self,
        investigation
    ):

        return (
            f"Investigation detected "
            f"{len(investigation.evidence)} "
            f"security artifacts requiring analysis."
        )



    def get_severity(
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