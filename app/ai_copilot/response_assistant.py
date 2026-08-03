from datetime import datetime


class ResponseAssistant:
    """
    Generates incident response recommendations.
    """


    def recommend(
        self,
        incident
    ):


        actions = [

            "Isolate affected systems",

            "Block malicious indicators",

            "Preserve forensic evidence",

            "Begin recovery workflow"

        ]


        if "ransomware" not in incident.lower():

            actions.remove(
                "Begin recovery workflow"
            )



        return {

            "incident":
                incident,

            "recommended_actions":
                actions,

            "timestamp":
                datetime.utcnow().isoformat()

        }