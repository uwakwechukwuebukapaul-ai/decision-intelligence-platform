class TaskRouter:
    """
    Routes SOC tasks to the correct AI agent.
    """


    def route(
        self,
        task
    ):

        task_type = task.get(
            "type",
            "unknown"
        )


        if task_type == "threat_hunting":

            return "threat_hunter"



        if task_type == "incident_response":

            return "incident_commander"



        if task_type == "detection":

            return "detection_engineer"



        return "general_agent"