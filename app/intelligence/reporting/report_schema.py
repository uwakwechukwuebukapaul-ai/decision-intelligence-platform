"""
Sentinel DNA Investigation Report Schema

Defines standardized SOC investigation reports.
"""


from datetime import datetime



class InvestigationReport:


    def __init__(
        self,
        indicator: str,
        severity: str,
        summary: str,
        technical_analysis: dict,
        recommendations: list,
    ):

        self.report_type = "IOC Investigation Report"

        self.generated_at = datetime.utcnow().isoformat()

        self.indicator = indicator

        self.severity = severity

        self.summary = summary

        self.technical_analysis = technical_analysis

        self.recommendations = recommendations



    def to_dict(self):

        return {

            "report_type":
                self.report_type,

            "generated_at":
                self.generated_at,

            "indicator":
                self.indicator,

            "severity":
                self.severity,

            "summary":
                self.summary,

            "technical_analysis":
                self.technical_analysis,

            "recommendations":
                self.recommendations,

        }