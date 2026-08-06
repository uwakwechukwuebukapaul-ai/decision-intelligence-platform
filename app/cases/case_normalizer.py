"""
Sentinel DNA - Case Intelligence Normalizer

Transforms multiple intelligence outputs into
a unified SOC incident object.

Responsibilities:

- Normalize risk
- Calculate confidence
- Extract MITRE techniques
- Generate priority
- Prepare analyst-ready case intelligence
"""


from __future__ import annotations


from datetime import datetime





class CaseNormalizer:
    """
    Converts investigation intelligence into
    standardized incident format.
    """



    def normalize(
        self,
        intelligence: dict,
        autonomous: dict | None = None,
        copilot: dict | None = None,
    ) -> dict:


        risk = intelligence.get(
            "risk",
            {}
        )


        campaign = intelligence.get(
            "campaign",
            {}
        )


        mitre = []


        for item in campaign.get(
            "techniques",
            []
        ):

            mitre.append(
                {
                    "technique_id":
                    item.get("technique_id"),

                    "technique":
                    item.get("technique"),
                }
            )



        risk_score = risk.get(
            "score",
            0
        )


        confidence = 0


        if autonomous:

            confidence = autonomous.get(
                "confidence",
                0
            )


        if confidence == 0 and copilot:

            confidence = copilot.get(
                "confidence",
                0
            )



        severity = self._severity(
            risk_score
        )


        priority = self._priority(
            risk_score
        )



        return {

            "incident_model":
            "sentinel-dna-incident-v1",


            "severity":
            severity,


            "priority":
            priority,


            "risk_score":
            risk_score,


            "confidence":
            confidence,


            "mitre":
            mitre,


            "recommendation":
            self._recommendation(
                severity
            ),


            "created_at":
            datetime.utcnow().isoformat(),

        }




    def _severity(
        self,
        score: int,
    ) -> str:


        if score >= 80:
            return "critical"


        if score >= 60:
            return "high"


        if score >= 40:
            return "medium"


        return "low"





    def _priority(
        self,
        score: int,
    ) -> str:


        if score >= 80:
            return "P1"


        if score >= 60:
            return "P2"


        if score >= 40:
            return "P3"


        return "P4"





    def _recommendation(
        self,
        severity: str,
    ) -> str:


        actions = {

            "critical":
            "Immediate containment and response required",

            "high":
            "Investigate indicator and validate enterprise impact",

            "medium":
            "Perform additional threat analysis",

            "low":
            "Monitor activity",

        }


        return actions.get(
            severity,
            "Review investigation"
        )