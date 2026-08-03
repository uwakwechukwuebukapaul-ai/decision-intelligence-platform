from datetime import datetime


class SPLGenerator:

    def generate(self, threat):

        return {
            "platform": "Splunk",
            "query":
                'index=security powershell OR ransomware',
            "timestamp": datetime.utcnow().isoformat()
        }