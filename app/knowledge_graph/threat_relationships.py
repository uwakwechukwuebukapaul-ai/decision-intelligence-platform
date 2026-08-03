from datetime import datetime


class ThreatRelationshipManager:


    def analyze(self,event):

        return {

            "relationships":[

                "Threat Actor -> Malware",

                "Malware -> Technique",

                "Technique -> Asset"

            ],

            "confidence":
                "high",

            "timestamp":
                datetime.utcnow().isoformat()

        }