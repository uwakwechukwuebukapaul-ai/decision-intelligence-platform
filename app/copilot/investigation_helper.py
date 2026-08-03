from datetime import datetime


class InvestigationHelper:
    """
    Helps analysts investigate incidents.
    """

    def guide(self, incident):

        steps = [

            "Collect available evidence",

            "Identify indicators of compromise",

            "Analyze attacker behaviour",

            "Map activity to MITRE ATT&CK",

            "Recommend response actions"

        ]


        return {

            "incident":
                incident,

            "investigation_steps":
                steps,

            "timestamp":
                datetime.utcnow().isoformat()

        }