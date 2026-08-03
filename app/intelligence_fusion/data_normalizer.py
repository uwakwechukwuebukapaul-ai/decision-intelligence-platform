from datetime import datetime


class DataNormalizer:
    """
    Normalizes security data from different Sentinel DNA engines.
    """

    def normalize(self, data):

        normalized = {
            "source": data.get("source", "unknown")
            if isinstance(data, dict)
            else "unknown",

            "event": data.get("event", data)
            if isinstance(data, dict)
            else data,

            "severity": data.get("severity", "unknown")
            if isinstance(data, dict)
            else "unknown",

            "timestamp": datetime.utcnow().isoformat()
        }

        return {
            "normalized_data": normalized,
            "status": "completed"
        }