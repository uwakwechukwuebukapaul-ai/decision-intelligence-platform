from datetime import datetime


class EntityExtractor:
    """
    Extracts intelligence entities from security and business inputs.
    """

    def extract(self, text):

        entities = []

        keywords = {
            "ransomware": "Threat",
            "phishing": "Threat",
            "malware": "Threat",
            "credential": "Identity",
            "finance": "Business Asset",
            "server": "Infrastructure",
            "endpoint": "Endpoint",
            "soc": "Security Operation",
            "mitre": "Framework",
            "ai": "Technology"
        }

        content = text.lower()

        for keyword, category in keywords.items():

            if keyword in content:

                entities.append(
                    {
                        "name": keyword,
                        "type": category
                    }
                )

        return {
            "entities": entities,
            "count": len(entities),
            "timestamp": datetime.utcnow().isoformat()
        }