from datetime import datetime


class SigmaEngine:

    def create(self, rule):

        return {
            "format": "Sigma",
            "title": rule["rule_name"],
            "status": "experimental",
            "logsource": {
                "category": "security"
            },
            "created_at": datetime.utcnow().isoformat()
        }