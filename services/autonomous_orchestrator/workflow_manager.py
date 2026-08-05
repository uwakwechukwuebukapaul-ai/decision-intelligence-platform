class WorkflowManager:
    """
    Creates autonomous SOC investigation workflows.
    """


    def create_workflow(
        self,
        event,
        decision
    ):

        stages = [

            "threat_intelligence",

            "detection_analysis",

            "investigation",

            "attack_reasoning",

            "response_planning"

        ]


        if decision.get("priority") == "critical":

            stages.append(
                "automatic_containment"
            )


        return {

            "event":
                event,

            "priority":
                decision.get(
                    "priority"
                ),

            "stages":
                stages,

            "workflow_status":
                "created"

        }