class AnomalyDetector:
    """
    Detects suspicious behavior patterns.
    """

    def analyze(
        self,
        events
    ):

        findings = []


        for event in events:

            text = event.lower()


            if "encoded" in text:

                findings.append({

                    "finding":
                    "Encoded command detected",

                    "risk":
                    "high"

                })


            if "powershell" in text:

                findings.append({

                    "finding":
                    "PowerShell activity detected",

                    "risk":
                    "medium"

                })


            if "ransomware" in text:

                findings.append({

                    "finding":
                    "Possible ransomware behavior",

                    "risk":
                    "critical"

                })


        return findings