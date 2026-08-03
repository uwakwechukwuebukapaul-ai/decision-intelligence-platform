from datetime import datetime


class KQLGenerator:

    def generate(self, threat):

        return {
            "platform": "Microsoft Sentinel",
            "query": """
DeviceProcessEvents
| where ProcessCommandLine contains "powershell"
| where InitiatingProcessFileName contains "cmd"
""",
            "timestamp": datetime.utcnow().isoformat()
        }