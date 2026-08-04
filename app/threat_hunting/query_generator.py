from datetime import datetime


class QueryGenerator:

    def generate(self, event):

        queries = [
            "Search PowerShell execution events",
            "Search suspicious process creation",
            "Search ransomware file activity",
            "Search privilege escalation attempts",
            "Search abnormal authentication activity"
        ]

        return {
            "generated_queries": queries,
            "event": event,
            "timestamp": datetime.now().isoformat()
        }