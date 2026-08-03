from datetime import datetime


class IOCEnrichment:


    def enrich(self, iocs):

        return {

            "enriched_indicators":
                iocs["indicators"],

            "context":
                [
                    "Geolocation",
                    "Threat category",
                    "Historical activity"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }