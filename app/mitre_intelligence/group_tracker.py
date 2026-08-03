from datetime import datetime


class GroupTracker:


    def identify(self, incident):

        groups = []


        text = incident.lower()


        if "ransomware" in text:
            groups.append(
                "Ransomware Associated Threat Groups"
            )


        return {
            "groups": groups,
            "count": len(groups),
            "timestamp": datetime.now().isoformat()
        }