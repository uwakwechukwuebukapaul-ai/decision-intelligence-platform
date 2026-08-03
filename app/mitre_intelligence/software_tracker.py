from datetime import datetime


class SoftwareTracker:


    def identify(self, incident):

        software = []

        text = incident.lower()


        if "powershell" in text:
            software.append(
                "PowerShell"
            )


        if "ransomware" in text:
            software.append(
                "Ransomware Malware Family"
            )


        return {
            "software": software,
            "count": len(software),
            "timestamp": datetime.now().isoformat()
        }