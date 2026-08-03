from datetime import datetime


class QueryHunter:

    def build(self, threat):

        return {
            "queries": {
                "sentinel": 
                f"SecurityEvent | where Message contains '{threat}'",

                "splunk":
                f"search threat='{threat}'",

                "elastic":
                f"event.message:{threat}"
            },
            "targets": [
                "Microsoft Sentinel",
                "Splunk",
                "Elastic Security"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }