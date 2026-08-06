class CopilotRepository:


    def __init__(self):

        self.reports = []



    def save(self, report):

        self.reports.append(report)

        return report



    def get_all(self):

        return self.reports



    def get_by_incident(
        self,
        incident_id
    ):

        return [

            report

            for report in self.reports

            if report["incident_id"] == incident_id

        ]