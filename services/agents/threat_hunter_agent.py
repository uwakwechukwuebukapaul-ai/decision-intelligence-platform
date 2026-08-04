from .base_agent import BaseAgent


class ThreatHunterAgent(BaseAgent):
    """
    Autonomous threat hunting agent.

    Generates investigation hypotheses.
    """


    def __init__(self):

        super().__init__(
            "threat_hunter"
        )


    def execute(
        self,
        context
    ):

        event = context.get(
            "event",
            ""
        )


        findings = []


        if "PowerShell" in event:

            findings.append(
                "Suspicious PowerShell execution detected"
            )


        if "ransomware" in event.lower():

            findings.append(
                "Potential ransomware behaviour identified"
            )


        return {

            "agent":
                self.name,

            "hypothesis":
                "Investigate attacker execution chain",

            "findings":
                findings,

            "timestamp":
                self.timestamp()

        }