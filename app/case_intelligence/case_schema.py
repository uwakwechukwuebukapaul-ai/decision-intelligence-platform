from datetime import datetime
import uuid


def create_case(
    title,
    severity="medium",
    source="AI_ENGINE"
):

    return {
        "case_id": f"CASE-{uuid.uuid4().hex[:8].upper()}",
        "title": title,
        "severity": severity,
        "status": "open",
        "assigned_to": None,
        "source": source,
        "evidence": [],
        "notes": [],
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }