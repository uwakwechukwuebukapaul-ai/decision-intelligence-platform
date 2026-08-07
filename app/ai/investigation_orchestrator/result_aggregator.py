class InvestigationResultAggregator:

    def aggregate(self, investigation):
        """
        Combine AI agent outputs into
        a unified investigation intelligence report.
        """

        return {
            "investigation_id": investigation.investigation_id,
            "severity": self._calculate_severity(
                investigation.state.risk_score
            ),
            "risk_score": investigation.state.risk_score,
            "confidence": investigation.state.confidence_score,
            "classification": investigation.state.classification,
            "findings": investigation.state.findings,
            "recommendations": investigation.state.recommendations,
        }


    def _calculate_severity(self, score):

        if score >= 80:
            return "CRITICAL"

        if score >= 60:
            return "HIGH"

        if score >= 30:
            return "MEDIUM"

        return "LOW"