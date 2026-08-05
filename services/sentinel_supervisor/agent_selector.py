class AgentSelector:
    """
    Selects the correct autonomous agents.
    """

    def select(self, incident):

        incident = incident.lower()

        agents = []

        if any(
            x in incident
            for x in [
                "malware",
                "ransomware",
                "exploit",
            ]
        ):
            agents.append(
                "ThreatHunterAgent"
            )

        if any(
            x in incident
            for x in [
                "attack",
                "breach",
                "intrusion",
            ]
        ):
            agents.append(
                "InvestigationAgent"
            )

        if "detection" in incident:
            agents.append(
                "DetectionEngineerAgent"
            )

        if any(
            x in incident
            for x in [
                "contain",
                "response",
            ]
        ):
            agents.append(
                "ResponseAgent"
            )


        if not agents:
            agents.append(
                "InvestigationAgent"
            )


        return agents