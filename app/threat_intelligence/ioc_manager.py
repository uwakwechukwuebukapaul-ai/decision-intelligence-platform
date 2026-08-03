from datetime import datetime
import re


class IOCManager:


    def extract(self, event):

        ips = re.findall(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            event
        )

        domains = re.findall(
            r"\b[a-zA-Z0-9.-]+\.(?:com|net|org|xyz|ru|top)\b",
            event
        )


        indicators = []

        indicators.extend(
            ips
        )

        indicators.extend(
            domains
        )


        return {

            "indicators":
                indicators,

            "types":
                [
                    "IP Address",
                    "Domain",
                    "Hash"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }