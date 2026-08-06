import uuid

from .evidence_collector import EvidenceCollector
from .evidence_correlator import EvidenceCorrelator
from .evidence_repository import EvidenceRepository
from .evidence_schema import Evidence, timestamp



class EvidenceEngine:


    def __init__(self):

        self.collector = EvidenceCollector()

        self.correlator = EvidenceCorrelator()

        self.repository = EvidenceRepository()



    def analyze(self, incident):


        collected = self.collector.collect(
            incident
        )


        findings = self.correlator.correlate(
            collected
        )


        evidence = Evidence(

            evidence_id=f"EVD-{uuid.uuid4().hex[:8].upper()}",

            incident_id=incident.get(
                "incident_id"
            ),

            evidence_type="security_event",

            source="Sentinel_DNA",

            confidence=0.95,

            created_at=timestamp()
        )


        self.repository.save(
            evidence.to_dict()
        )


        return {

            "evidence_id": evidence.evidence_id,

            "incident_id": evidence.incident_id,

            "collected_evidence": collected,

            "findings": findings,

            "confidence": evidence.confidence,

            "created_at": evidence.created_at
        }