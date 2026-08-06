from datetime import datetime
import uuid


def create_posture_record(
    organization,
    score,
    level,
    findings,
    recommendations
):
    return {
        "posture_id": f"POSTURE-{uuid.uuid4().hex[:8].upper()}",
        "organization": organization,
        "security_score": score,
        "security_level": level,
        "findings": findings,
        "recommendations": recommendations,
        "created_at": datetime.utcnow().isoformat()
    }