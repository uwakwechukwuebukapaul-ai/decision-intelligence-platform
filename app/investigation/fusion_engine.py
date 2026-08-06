"""
Sentinel DNA Fusion Engine

Combines:
- Incident data
- Evidence
- Timeline
- Threat intelligence
- AI reasoning
"""


from datetime import datetime

from .fusion_schema import FusionResult

from .investigation_service import InvestigationService

from app.threat_intelligence import IntelligenceManager




class FusionEngine:


    def __init__(self):

        self.investigation = InvestigationService()

        self.intelligence = IntelligenceManager()



    def analyze(
        self,
        incident_id: str
    ):


        context = self.investigation.get_investigation(
            incident_id
        )


        incident = context.get(
            "incident",
            {}
        )


        indicator = incident.get(
            "indicator"
        )


        intel = {}

        if indicator:

            intel = self.intelligence.enrich(
                indicator
            )


        evidence = context.get(
            "evidence",
            []
        )


        timeline = context.get(
            "timeline",
            []
        )


        findings = []


        if intel.get(
            "threat_level"
        ) == "high":

            findings.append(
                "High risk IOC detected"
            )


        if len(evidence):

            findings.append(
                "Evidence correlated with incident"
            )


        recommendations = [

            "Block malicious indicator",

            "Perform threat hunting",

            "Collect endpoint telemetry"

        ]


        return FusionResult(

            incident_id=incident_id,

            incident=incident,

            threat_intelligence=intel,

            evidence_count=len(evidence),

            timeline_count=len(timeline),

            findings=findings,

            recommendations=recommendations,

            risk_summary=
                "Threat intelligence fusion completed"

        ).__dict__