from datetime import datetime
import uuid


def create_dashboard_id():
    return f"DASH-{uuid.uuid4().hex[:8].upper()}"


def dashboard_record(
    organization,
    security_score,
    risk_level,
    metrics,
    recommendations
):
    return {
        "dashboard_id": create_dashboard_id(),
        "organization": organization,
        "security_score": security_score,
        "risk_level": risk_level,
        "metrics": metrics,
        "recommendations": recommendations,
        "created_at": datetime.utcnow().isoformat()
    }