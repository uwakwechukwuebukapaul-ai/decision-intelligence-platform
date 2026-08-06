class SOARRepository:


    def __init__(self):

        self.executions = []



    def save(
        self,
        execution
    ):

        self.executions.append(
            execution
        )

        return execution



    def get_all(self):

        return self.executions



    def get_by_incident(
        self,
        incident_id
    ):

        return [
            execution
            for execution in self.executions
            if execution["incident_id"] == incident_id
        ]