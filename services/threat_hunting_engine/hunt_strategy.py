class HuntStrategy:
    """
    Creates threat hunting objectives
    from security observations.
    """

    def __init__(self):

        self.strategies = {

            "powershell": {
                "objective": "Detect suspicious PowerShell execution",
                "techniques": [
                    "T1059.001",
                    "Command and Scripting Interpreter: PowerShell"
                ]
            },

            "ransomware": {
                "objective": "Identify ransomware behavior patterns",
                "techniques": [
                    "T1486",
                    "Data Encrypted for Impact"
                ]
            },

            "credential": {
                "objective": "Find credential abuse activity",
                "techniques": [
                    "T1003",
                    "OS Credential Dumping"
                ]
            },

            "lateral": {
                "objective": "Detect lateral movement attempts",
                "techniques": [
                    "T1021",
                    "Remote Services"
                ]
            }
        }


    def generate(self, event):

        event_lower = event.lower()

        hunts = []


        for keyword, strategy in self.strategies.items():

            if keyword in event_lower:

                hunts.append({

                    "objective":
                    strategy["objective"],

                    "mitre_techniques":
                    strategy["techniques"],

                    "priority":
                    "high"

                })


        if not hunts:

            hunts.append({

                "objective":
                "General anomaly threat hunt",

                "mitre_techniques":
                [],

                "priority":
                "medium"

            })


        return hunts