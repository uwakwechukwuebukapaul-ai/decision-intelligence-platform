from datetime import datetime


class FrameworkMapper:

    def map_frameworks(self, incident):

        return {
            "incident": incident,
            "frameworks": {
                "NIST_CSF": [
                    "Identify",
                    "Protect",
                    "Detect",
                    "Respond",
                    "Recover"
                ],
                "ISO_27001": [
                    "Risk Management",
                    "Security Controls"
                ],
                "SOC_2": [
                    "Security",
                    "Availability"
                ]
            },
            "timestamp": datetime.utcnow().isoformat()
        }