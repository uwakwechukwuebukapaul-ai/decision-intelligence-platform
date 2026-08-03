from datetime import datetime


class ActorTracker:
    """
    Tracks threat actors.
    """


    def identify(
        self,
        activity
    ):

        actors = []


        if "ransomware" in activity.lower():

            actors.append(
                "Ransomware Threat Actor"
            )


        return {

            "activity":
                activity,

            "actors":
                actors,

            "count":
                len(actors),

            "timestamp":
                datetime.utcnow().isoformat()

        }