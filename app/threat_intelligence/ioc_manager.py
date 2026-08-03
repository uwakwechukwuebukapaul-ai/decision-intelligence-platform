from datetime import datetime
import re
import uuid


class IOCManager:


    def extract(self, event):

        indicators = []


        urls = re.findall(
            r"https?://\S+",
            event
        )


        for url in urls:

            indicators.append(
                {
                    "type": "URL",
                    "value": url,
                    "risk": "high"
                }
            )


        if "PowerShell" in event:

            indicators.append(
                {
                    "type": "Technique Indicator",
                    "value": "PowerShell",
                    "risk": "medium"
                }
            )


        return {

            "ioc_id": "IOC-" + str(uuid.uuid4())[:8],

            "indicators": indicators,

            "timestamp": datetime.utcnow().isoformat()

        }