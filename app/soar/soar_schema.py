from datetime import datetime
import uuid


def create_execution(
    incident_id,
    playbook,
    actions,
    status
):

    return {
        "execution_id": f"SOAR-{uuid.uuid4().hex[:8].upper()}",
        "incident_id": incident_id,
        "playbook": playbook,
        "actions": actions,
        "status": status,
        "created_at": datetime.utcnow().isoformat()
    }