class TaskRouter:
    """
    Routes SOC tasks to appropriate agents.
    """

    def __init__(self):

        self.routes = {

            "investigation":
                "investigation_agent",

            "threat_hunting":
                "threat_hunter",

            "response":
                "response_agent",

            "analysis":
                "analysis_agent"
        }


    def route(
        self,
        task_type
    ):

        return self.routes.get(
            task_type,
            "general_agent"
        )


    def add_route(
        self,
        task_type,
        agent_name
    ):

        self.routes[task_type] = agent_name