from datetime import datetime


class QueryBuilder:

    def build(self, threat):

        return {
            "siem_queries": {
                "splunk": f"search suspicious_activity='{threat}'",
                "kql": f"SecurityEvent | where Message contains '{threat}'",
                "elastic": f"event.message:{threat}"
            },
            "targets": [
                "Splunk",
                "Microsoft Sentinel",
                "Elastic Security"
            ],
            "created_at": datetime.utcnow().isoformat()
        }