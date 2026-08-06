from datetime import datetime
import uuid


def create_audit_event(
    incident_id,
    event_type,
    action,
    actor="system",
    details=None
):
    return {
        "audit_id": f"AUD-{uuid.uuid4().hex[:8]}",
        "incident_id": incident_id,
        "event_type": event_type,
        "action": action,
        "actor": actor,
        "details": details or {},
        "created_at": datetime.utcnow().isoformat()
    }