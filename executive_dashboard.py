class ExecutiveDashboard:

    def __init__(self):
        self.metrics = {}


    def update_metrics(self, metrics):

        self.metrics = metrics

        return self.metrics


    def get_metrics(self):

        return self.metrics