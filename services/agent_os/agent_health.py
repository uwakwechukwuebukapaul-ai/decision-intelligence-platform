class AgentHealth:
    """
    Agent availability and health monitoring.
    """


    def __init__(self):

        self.health = {}


    def register_agent(
        self,
        agent
    ):

        self.health[agent] = {

            "status":
                "healthy",

            "failures":
                0,

            "executions":
                0

        }


        return self.health[agent]


    def record_execution(
        self,
        agent
    ):

        if agent not in self.health:

            self.register_agent(
                agent
            )


        self.health[agent]["executions"] += 1


        return self.health[agent]


    def record_failure(
        self,
        agent
    ):

        if agent not in self.health:

            self.register_agent(
                agent
            )


        self.health[agent]["failures"] += 1


        if self.health[agent]["failures"] >= 3:

            self.health[agent]["status"] = "degraded"


        return self.health[agent]


    def status(
        self,
        agent=None
    ):

        if agent:

            return self.health.get(
                agent
            )


        return self.health