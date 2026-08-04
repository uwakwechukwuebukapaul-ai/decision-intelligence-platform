from datetime import datetime, timezone


class WorkflowStateManager:
    """
    Manages autonomous SOC workflow states.

    Responsible for tracking:
    - lifecycle changes
    - timestamps
    - execution history
    """


    VALID_STATES = [

        "created",

        "investigating",

        "decision_pending",

        "response_ready",

        "executing",

        "completed",

        "failed"

    ]


    def __init__(self):

        self.history = []



    def update_state(
        self,
        workflow,
        new_state
    ):

        if new_state not in self.VALID_STATES:

            raise ValueError(
                f"Invalid workflow state: {new_state}"
            )


        previous_state = workflow.state


        workflow.state = new_state


        event = {

            "workflow_id":
                workflow.workflow_id,

            "previous_state":
                previous_state,

            "new_state":
                new_state,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.history.append(
            event
        )


        return workflow



    def get_history(self):

        return self.history