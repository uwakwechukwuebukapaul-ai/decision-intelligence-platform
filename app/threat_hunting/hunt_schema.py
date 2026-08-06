from datetime import datetime
import uuid


def create_hunt(
    indicator,
    hypothesis,
    queries,
    mitre_mapping
):

    return {

        "hunt_id": f"HUNT-{uuid.uuid4().hex[:8].upper()}",

        "indicator": indicator,

        "hypothesis": hypothesis,

        "queries": queries,

        "mitre_mapping": mitre_mapping,

        "status": "active",

        "created_at": datetime.utcnow().isoformat()

    }