from datetime import datetime


def create_response_schema(
    incident_id,
    action,
    status,
    details=None
):

    return {

        "response_id":
            f"RESP-{incident_id}",

        "incident_id":
            incident_id,

        "action":
            action,

        "status":
            status,

        "details":
            details or {},

        "created_at":
            datetime.utcnow().isoformat()
    }