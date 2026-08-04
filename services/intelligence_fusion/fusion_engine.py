from services.intelligence_fusion.context_builder import ContextBuilder
from services.intelligence_fusion.intelligence_model import IntelligenceModel


class IntelligenceFusionEngine:
    """
    Intelligence Fusion Layer.

    Combines:
    - Evidence intelligence
    - Detection intelligence
    - Threat intelligence
    - Cognitive risk intelligence

    Produces a unified intelligence response.
    """


    def __init__(self):

        self.context_builder = ContextBuilder()



    def classify(
        self,
        event,
        threat=None
    ):

        threat = threat or {}

        malware = threat.get(
            "malware",
            ""
        )


        if malware:

            return "malware_activity"


        if "ransomware" in event.lower():

            return "ransomware_attack"


        if "phishing" in event.lower():

            return "phishing_attack"


        return "unknown"



    def calculate_confidence(
        self,
        context,
        evidence,
        detection
    ):

        score = 0


        if context.entities:

            score += 0.3


        if context.relationships:

            score += 0.2


        if evidence:

            score += 0.3


        if detection:

            score += 0.2


        return min(
            score,
            1.0
        )



    def fuse(
        self,
        event,
        evidence=None,
        detection=None,
        threat=None,
        cognitive=None
    ):

        evidence = evidence or {}

        detection = detection or {}

        threat = threat or {}

        cognitive = cognitive or {}



        context = self.context_builder.build(
            event
        )



        risk_score = evidence.get(
            "risk_score",
            0
        )



        classification = self.classify(
            event,
            threat
        )



        confidence = self.calculate_confidence(
            context,
            evidence,
            detection
        )



        intelligence = IntelligenceModel(

            event=event,

            entities=context.entities,

            relationships=context.relationships,

            threats=[

                {
                    "name": threat.get(
                        "malware",
                        "unknown"
                    ),

                    "severity": cognitive.get(
                        "risk_level",
                        "unknown"
                    )
                }

            ],

            confidence=confidence,

            risk_score=risk_score,

            classification=classification,

            recommendations=[

                "Investigate affected systems",

                "Review detection telemetry",

                "Correlate threat intelligence"

            ]

        )



        return {

            "status": "completed",

            "risk": {

                "risk_level": cognitive.get(
                    "risk_level",
                    "unknown"
                ),

                "risk_score": risk_score

            },

            "intelligence": intelligence.to_dict()

        }



    def analyze(
        self,
        event
    ):

        return self.fuse(
            event
        )