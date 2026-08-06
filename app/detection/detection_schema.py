from datetime import datetime


def create_detection_schema(data):

    return {
        "detection_id": data.get(
            "detection_id"
        ),

        "incident_id": data.get(
            "incident_id"
        ),

        "rule": data.get(
            "rule"
        ),

        "severity": data.get(
            "severity",
            "medium"
        ),

        "indicator": data.get(
            "indicator"
        ),

        "status": data.get(
            "status",
            "new"
        ),

        "created_at": data.get(
            "created_at",
            datetime.utcnow().isoformat()
        )
    }