class AgentCoordinator:

    def select_agents(self, context):

        agents = []

        if context["threat_indicators"]:
            agents.extend(
                [
                    "ThreatHunter",
                    "EvidenceFusion",
                    "InvestigationReasoner"
                ]
            )

        return agents