from datetime import datetime


class KQLGenerator:

    def generate(self, event):

        return {
            "query_language": "KQL",
            "query": """
DeviceProcessEvents
| where ProcessCommandLine contains "powershell"
| where FileName contains "encrypt"
""",
            "timestamp": datetime.utcnow().isoformat()
        }