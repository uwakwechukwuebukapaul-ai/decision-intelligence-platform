from datetime import datetime
import uuid


class ExecutionMemory:


    def __init__(self):

        self.executions = []



    def store(
        self,
        execution
    ):

        record = {

            "execution_id":
                "EXEC-" + str(uuid.uuid4())[:8].upper(),

            "execution":
                execution,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.executions.append(
            record
        )


        return {

            "status":
                "stored",

            "execution":
                record

        }



    def get_history(
        self
    ):

        return {

            "count":
                len(self.executions),

            "executions":
                self.executions

        }