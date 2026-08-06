"""
Sentinel DNA Hunt Schema

Threat hunting result structures.
"""

from datetime import datetime


def create_hunt_result(
    query,
    findings,
    severity="medium"
):

    return {

        "hunt_id":
            f"HUNT-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

        "query":
            query,

        "findings":
            findings,

        "severity":
            severity,

        "created_at":
            datetime.utcnow().isoformat()

    }