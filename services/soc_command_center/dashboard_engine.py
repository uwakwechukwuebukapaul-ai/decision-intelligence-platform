class DashboardEngine:
    """
    Central SOC Command Center dashboard controller.

    Aggregates:
    - threats
    - investigations
    - risks
    - agents
    """


    def generate(
        self,
        security_data=None
    ):

        security_data = security_data or {}

        return {

            "status": "dashboard_ready",

            "overview": {

                "active_threats":
                    len(
                        security_data.get(
                            "threats",
                            []
                        )
                    ),

                "active_cases":
                    len(
                        security_data.get(
                            "cases",
                            []
                        )
                    ),

                "running_agents":
                    len(
                        security_data.get(
                            "agents",
                            []
                        )
                    )

            },

            "data": security_data

        }