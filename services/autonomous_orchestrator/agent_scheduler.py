class AgentScheduler:
    """
    Schedules Sentinel DNA AI agents.
    """


    def schedule(
        self,
        workflow
    ):

        agents = []


        for stage in workflow["stages"]:

            if stage == "threat_intelligence":
                agents.append(
                    "Threat Intelligence Agent"
                )

            elif stage == "detection_analysis":
                agents.append(
                    "Detection Engineering Agent"
                )

            elif stage == "investigation":
                agents.append(
                    "Investigation AI Agent"
                )

            elif stage == "attack_reasoning":
                agents.append(
                    "Attack Reasoning Agent"
                )

            elif stage == "response_planning":
                agents.append(
                    "Response Intelligence Agent"
                )

            elif stage == "automatic_containment":
                agents.append(
                    "Containment Agent"
                )


        return agents