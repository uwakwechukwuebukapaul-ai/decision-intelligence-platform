from datetime import datetime


class ThreatView:


    def generate(self, incident):

        threats = []


        if "ransomware" in incident.lower():

            threats.append(
                "Ransomware activity"
            )


        if "powershell" in incident.lower():

            threats.append(
                "PowerShell execution"
            )


        return {

            "identified_threats":

                threats,

            "threat_level":

                "critical",

            "timestamp":

                datetime.utcnow().isoformat()
        }