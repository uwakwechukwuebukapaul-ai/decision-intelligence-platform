class HypothesisEngine:
    """
    Generates possible attack hypotheses
    from security events.
    """

    def __init__(self):

        self.patterns = {

            "ransomware": {
                "hypothesis": "Possible ransomware execution chain",
                "evidence": [
                    "file modification events",
                    "process execution logs",
                    "endpoint telemetry"
                ]
            },

            "powershell": {
                "hypothesis": "Possible PowerShell based execution",
                "evidence": [
                    "PowerShell logs",
                    "command history",
                    "process tree"
                ]
            },

            "credential": {
                "hypothesis": "Possible credential compromise",
                "evidence": [
                    "authentication logs",
                    "identity events",
                    "privilege changes"
                ]
            }

        }


    def generate(
        self,
        event
    ):

        event_lower = event.lower()

        hypotheses = []


        for keyword, data in self.patterns.items():

            if keyword in event_lower:

                hypotheses.append({

                    "hypothesis": data["hypothesis"],

                    "confidence": 0.85,

                    "required_evidence": data["evidence"]

                })


        if not hypotheses:

            hypotheses.append({

                "hypothesis": "Unknown security incident pattern",

                "confidence": 0.40,

                "required_evidence": [
                    "logs",
                    "network telemetry",
                    "endpoint data"
                ]

            })


        return hypotheses