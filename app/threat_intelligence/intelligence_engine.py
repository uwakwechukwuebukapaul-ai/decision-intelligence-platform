from datetime import datetime

from .ioc_enrichment import IOCEnrichment
from .source_connector import SourceConnector
from .intelligence_repository import IntelligenceRepository


class IntelligenceEngine:


    def __init__(self):

        self.enrichment = IOCEnrichment()
        self.connector = SourceConnector()
        self.repository = IntelligenceRepository()



    def analyze(self, ioc):

        enrichment = self.enrichment.enrich(ioc)

        source_data = self.connector.query(ioc)


        risk_score = 20

        if enrichment["reputation"] == "malicious":
            risk_score = 90

        elif enrichment["tags"]:
            risk_score = 70


        threat_level = "low"

        if risk_score >= 90:
            threat_level = "critical"

        elif risk_score >= 70:
            threat_level = "high"


        result = {

            "ioc": ioc,

            "type": enrichment["category"],

            "threat_level": threat_level,

            "risk_score": risk_score,

            "confidence": source_data["confidence"],

            "tags": enrichment["tags"],

            "source": source_data["source"],

            "created_at": datetime.utcnow().isoformat()

        }


        self.repository.save(result)


        return result