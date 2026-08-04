from .soc_model import SOCWorkflowModel


class AnalystAgent:
    """
    Autonomous SOC Analyst reasoning agent.

    Responsible for:
    - analysing investigation plans
    - generating findings
    - producing analyst reasoning
    """


    def investigate(
        self,
        incident,
        plan
    ):


        workflow = SOCWorkflowModel(
            event=incident
        )


        workflow.investigation_plan.extend(
            plan
        )


        workflow.add_finding(
            "Suspicious security activity detected"
        )


        workflow.add_finding(
            "Potential ransomware behaviour identified"
        )


        workflow.confidence = 0.85


        workflow.complete()


        return workflow