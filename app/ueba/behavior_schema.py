from datetime import datetime
import uuid


def create_behavior_event(
    username,
    event_type,
    details
):

    return {

        "event_id":
            f"BEH-{uuid.uuid4().hex[:8]}",

        "username":
            username,

        "event_type":
            event_type,

        "details":
            details,

        "created_at":
            datetime.utcnow().isoformat()

    }