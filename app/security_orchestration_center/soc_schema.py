from datetime import datetime
import uuid


def create_soc_record(
    incident_id,
    priority,
    workflow,
    agents,
    status
):
    return {
        "soc_id": f"SOC-{uuid.uuid4().hex[:8].upper()}",
        "incident_id": incident_id,
        "priority": priority,
        "workflow": workflow,
        "agents": agents,
        "status": status,
        "created_at": datetime.utcnow().isoformat()
    }