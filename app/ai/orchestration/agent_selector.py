class AgentSelector:
    """
    Selects the correct AI agents for a mission.
    """


    def select_agents(
        self,
        objective
    ):

        objective = objective.lower()


        agents = []


        if any(
            word in objective
            for word in [
                "research",
                "market",
                "analysis",
                "intelligence"
            ]
        ):

            agents.append(
                "Research Agent"
            )


        if any(
            word in objective
            for word in [
                "forecast",
                "prediction",
                "future",
                "trend"
            ]
        ):

            agents.append(
                "Forecasting Agent"
            )


        if any(
            word in objective
            for word in [
                "decision",
                "strategy",
                "opportunity",
                "recommend"
            ]
        ):

            agents.append(
                "Decision Agent"
            )


        if not agents:

            agents = [
                "Research Agent",
                "Decision Agent"
            ]


        return agents