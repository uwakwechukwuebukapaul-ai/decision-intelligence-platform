from datetime import datetime
import uuid


class EvidenceRepository:
    """
    Stores investigation evidence.
    """

    def __init__(self):
        self.evidence = []

    def add_evidence(self, case_id, evidence_type, data):

        record = {
            "evidence_id": f"EVID-{uuid.uuid4().hex[:8].upper()}",
            "case_id": case_id,
            "type": evidence_type,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.evidence.append(record)

        return record


    def get_case_evidence(self, case_id):

        results = [
            item for item in self.evidence
            if item["case_id"] == case_id
        ]

        return {
            "case_id": case_id,
            "evidence_count": len(results),
            "evidence": results
        }