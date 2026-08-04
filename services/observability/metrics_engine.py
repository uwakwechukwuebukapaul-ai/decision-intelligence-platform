class MetricsEngine:

    def __init__(self):

        self.metrics = {
            "executions": {},
            "success": {},
            "failure": {}
        }


    def record_execution(self, service_name):

        if service_name not in self.metrics["executions"]:
            self.metrics["executions"][service_name] = 0

        self.metrics["executions"][service_name] += 1

        return self.metrics["executions"][service_name]


    def record_result(
        self,
        service_name,
        success=True
    ):

        target = (
            "success"
            if success
            else "failure"
        )

        if service_name not in self.metrics[target]:
            self.metrics[target][service_name] = 0

        self.metrics[target][service_name] += 1

        return self.metrics[target][service_name]


    def get_metrics(self):

        return self.metrics