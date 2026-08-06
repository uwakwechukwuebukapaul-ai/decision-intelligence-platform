from datetime import datetime
import uuid


def create_report(
    incident_id,
    summary,
    risk,
    recommendations,
    confidence
):

    return {

        "report_id": f"RPT-{uuid.uuid4().hex[:8].upper()}",

        "incident_id": incident_id,

        "summary": summary,

        "risk": risk,

        "recommendations": recommendations,

        "confidence": confidence,

        "created_at": datetime.utcnow().isoformat()

    }