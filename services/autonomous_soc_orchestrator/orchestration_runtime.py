import uuid
from datetime import datetime


class OrchestrationRuntime:


    def __init__(self):

        self.executions = {}



    def create_execution(
        self,
        event
    ):

        execution_id = (
            "SOC-"
            +
            str(uuid.uuid4())[:8]
        )


        self.executions[execution_id] = {

            "event": event,

            "started":

            datetime.utcnow().isoformat(),

            "status": "running"

        }


        return execution_id



    def complete_execution(
        self,
        execution_id,
        result
    ):

        if execution_id in self.executions:

            self.executions[execution_id][
                "result"
            ] = result


            self.executions[execution_id][
                "status"
            ] = "completed"