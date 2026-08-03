from datetime import datetime


class IOCEnricher:


    def enrich(self, iocs):

        return {
            "enriched_indicators": iocs["indicators"],
            "sources": [
                "Threat Intelligence Database",
                "Malware Intelligence",
                "IOC Repository"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }