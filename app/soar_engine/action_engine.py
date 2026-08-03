from datetime import datetime


class ActionEngine:
    """
    Generates security response actions.
    """


    def generate(
        self,
        incident
    ):


        actions = [

            "Collect forensic evidence",

            "Block malicious indicators",

            "Notify security team"

        ]


        if "ransomware" in incident.lower():

            actions.append(
                "Isolate affected endpoint"
            )



        return {

            "incident":
                incident,

            "actions":
                actions,

            "count":
                len(actions),

            "timestamp":
                datetime.utcnow().isoformat()

        }