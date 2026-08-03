from datetime import datetime


class ThreatView:
    """
    Displays threat intelligence summary.
    """


    def analyze(self, event):

        text = str(event).lower()


        threats = []


        if "ransomware" in text:
            threats.append(
                "Ransomware Campaign"
            )


        if "phishing" in text:
            threats.append(
                "Phishing Activity"
            )


        return {

            "identified_threats":
                threats,

            "count":
                len(threats),

            "framework":
                "MITRE ATT&CK",

            "timestamp":
                datetime.utcnow().isoformat()

        }