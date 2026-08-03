from datetime import datetime


class ThreatActorTracker:


    def analyze(self, event):

        actors = []

        if "ransomware" in event.lower():

            actors.append(
                "Ransomware Associated Groups"
            )


        return {

            "actors":
                actors,

            "campaign":
                "Ransomware Campaign Analysis",

            "timestamp":
                datetime.utcnow().isoformat()

        }