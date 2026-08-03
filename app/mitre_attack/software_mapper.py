from datetime import datetime


class SoftwareMapper:

    def map(self, event):

        software = []

        if "powershell" in event.lower():
            software.append("PowerShell")

        if "ransomware" in event.lower():
            software.append("Ransomware Family")

        return {
            "software": software,
            "timestamp": datetime.utcnow().isoformat()
        }