from .report_generator import ReportGenerator
from .copilot_repository import CopilotRepository
from .copilot_schema import create_report



class CopilotEngine:


    def __init__(self):

        self.generator = ReportGenerator()

        self.repository = CopilotRepository()



    def generate_report(
        self,
        incident
    ):

        incident_id = incident.get(
            "incident_id"
        )


        summary = self.generator.generate_summary(
            incident
        )


        risk = self.generator.generate_risk(
            incident
        )


        recommendations = self.generator.generate_recommendations(
            incident
        )


        report = create_report(

            incident_id,

            summary,

            risk,

            recommendations,

            0.85

        )


        return self.repository.save(
            report
        )



    def get_reports(self):

        return self.repository.get_all()



    def get_incident_report(
        self,
        incident_id
    ):

        return self.repository.get_by_incident(
            incident_id
        )