"""
Sentinel DNA - Incident Normalizer

Transforms investigation intelligence
into a unified SOC incident model.
"""


from __future__ import annotations


import uuid


from .incident_schema import Incident





class IncidentNormalizer:
    """
    Converts investigation results into
    standardized incident objects.
    """



    def normalize(
        self,
        investigation: dict,
    ) -> dict:
        """
        Build unified incident representation.
        """

        indicator = investigation.get(
            "indicator",
            "unknown"
        )


        intelligence = investigation.get(
            "intelligence",
            {}
        )


        risk = intelligence.get(
            "risk",
            {}
        )


        risk_score = risk.get(
            "score",
            0
        )


        severity = risk.get(
            "risk",
            "unknown"
        )


        confidence = investigation.get(
            "confidence",
            0
        )


        priority = self.calculate_priority(
            risk_score,
            severity,
        )


        mitre = []


        evidence = intelligence.get(
            "memory",
            []
        )


        if evidence:

            mitre = evidence[0].get(
                "mitre_mapping",
                []
            )



        recommendations = []


        recommendation = intelligence.get(
            "recommendation",
            {}
        )


        if recommendation:

            recommendations.append(
                recommendation.get(
                    "action",
                    "Review incident"
                )
            )



        incident = Incident(

            incident_id=f"INC-{uuid.uuid4().hex[:8].upper()}",

            indicator=indicator,

            severity=severity,

            priority=priority,

            risk_score=risk_score,

            confidence=confidence,

            mitre=mitre,

            evidence=intelligence,

            recommendations=recommendations,

        )


        return incident.to_dict()



    def calculate_priority(
        self,
        risk_score: int,
        severity: str,
    ) -> str:
        """
        Determine SOC priority.
        """


        if risk_score >= 80:

            return "P1"



        if risk_score >= 50:

            return "P2"



        if severity == "medium":

            return "P3"



        return "P4"