from datetime import datetime


class SPLGenerator:

    def generate(self, event):

        return {
            "query_language": "SPL",
            "query": """
index=security
ProcessName=powershell
| search encryption
""",
            "timestamp": datetime.utcnow().isoformat()
        }