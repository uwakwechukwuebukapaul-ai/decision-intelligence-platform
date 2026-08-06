from datetime import datetime

from .ioc_enrichment import IOCEnrichment
from .source_connector import SourceConnector
from .intelligence_repository import IntelligenceRepository


class IntelligenceEngine:
    """
    Sentinel DNA Threat Intelligence Engine

    Responsibilities:
    - IOC enrichment
    - Threat reputation analysis
    - Risk scoring
    - Intelligence source correlation
    - Repository persistence
    - Compatibility interface for investigation pipelines
    """


    def __init__(self):

        self.enrichment = IOCEnrichment()
        self.connector = SourceConnector()
        self.repository = IntelligenceRepository()



    def analyze(self, ioc):
        """
        Primary threat intelligence analysis pipeline.
        """

        enrichment = self.enrichment.enrich(ioc)

        source_data = self.connector.query(ioc)


        risk_score = 20


        if enrichment.get("reputation") == "malicious":

            risk_score = 90


        elif enrichment.get("tags"):

            risk_score = 70



        threat_level = "low"


        if risk_score >= 90:

            threat_level = "critical"


        elif risk_score >= 70:

            threat_level = "high"



        result = {

            "ioc": ioc,

            "type": enrichment.get("category"),

            "threat_level": threat_level,

            "risk_score": risk_score,

            "confidence": source_data.get(
                "confidence",
                0.5
            ),

            "tags": enrichment.get(
                "tags",
                []
            ),

            "source": source_data.get(
                "source",
                "unknown"
            ),

            "created_at": datetime.utcnow().isoformat()

        }


        self.repository.save(result)


        return result



    def enrich(self, ioc):
        """
        Compatibility API.

        Used by:
        - Investigation Fusion Engine
        - Correlation Engine
        - Automated Investigation Pipeline

        Maps the Threat Intelligence analysis
        response into enrichment format.
        """


        result = self.analyze(ioc)


        return {

            "ioc": result["ioc"],

            "type": result["type"],

            "threat_level": result["threat_level"],

            "risk_score": result["risk_score"],

            "confidence": result["confidence"],

            "tags": result["tags"],

            "source": result["source"],

            "details": {

                "message":
                "IOC threat intelligence enrichment completed"

            },

            "created_at": result["created_at"]

        }