from datetime import datetime
import uuid


def create_detection(
    indicator,
    rule_name,
    severity,
    confidence,
    mitre_techniques
):

    return {
        "detection_id": f"DET-{uuid.uuid4().hex[:8].upper()}",
        "indicator": indicator,
        "rule_name": rule_name,
        "severity": severity,
        "confidence": confidence,
        "mitre_techniques": mitre_techniques,
        "status": "active",
        "created_at": datetime.utcnow().isoformat()
    }