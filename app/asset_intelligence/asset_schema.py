"""
Sentinel DNA Asset Schema

Defines enterprise asset objects.
"""

from datetime import datetime
import uuid



def create_asset(
    hostname,
    ip_address=None,
    owner=None,
    asset_type="endpoint",
    criticality="medium"
):

    return {

        "asset_id":
            f"AST-{uuid.uuid4().hex[:8]}",

        "hostname":
            hostname,

        "ip_address":
            ip_address,

        "owner":
            owner,

        "asset_type":
            asset_type,

        "criticality":
            criticality,

        "risk_score":
            calculate_risk(
                criticality
            ),

        "created_at":
            datetime.utcnow().isoformat()

    }



def calculate_risk(
    criticality
):

    scores = {

        "low": 20,

        "medium": 50,

        "high": 80,

        "critical": 95

    }


    return scores.get(
        criticality,
        50
    )