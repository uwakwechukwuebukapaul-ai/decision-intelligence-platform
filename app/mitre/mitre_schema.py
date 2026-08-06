from datetime import datetime
import uuid


def create_mapping(
    indicator,
    technique,
    tactic,
    name,
    confidence,
    source="MITRE_ATT&CK",
):

    return {
        "mapping_id": f"MITRE-{uuid.uuid4().hex[:8].upper()}",
        "indicator": indicator,
        "technique": technique,
        "tactic": tactic,
        "name": name,
        "confidence": confidence,
        "source": source,
        "created_at": datetime.utcnow().isoformat(),
    }