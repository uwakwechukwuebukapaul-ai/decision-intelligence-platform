from datetime import datetime
import uuid


def create_evidence(
    case_id,
    value,
    evidence_type,
    source="AI_ENGINE"
):

    return {
        "evidence_id": f"EVD-{uuid.uuid4().hex[:8].upper()}",
        "case_id": case_id,
        "value": value,
        "type": evidence_type,
        "classification": classify_type(evidence_type),
        "source": source,
        "created_at": datetime.utcnow().isoformat()
    }



def classify_type(evidence_type):

    mapping = {

        "ioc": "indicator",
        "log": "telemetry",
        "identity": "identity_event",
        "file": "malware_artifact",
        "network": "network_artifact"

    }

    return mapping.get(
        evidence_type,
        "unknown"
    )