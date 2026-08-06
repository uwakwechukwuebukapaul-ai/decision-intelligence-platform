"""
Sentinel DNA Report Generator

Combines investigation intelligence
into a final SOC report.
"""


from .executive_summary import ExecutiveSummary
from .analyst_report import AnalystReport



class ReportGenerator:


    def __init__(self):

        self.summary = ExecutiveSummary()

        self.analyst = AnalystReport()



    def generate(
        self,
        investigation
    ):

        return {

            "executive_summary":
                self.summary.generate(
                    investigation
                ),


            "analyst_report":
                self.analyst.generate(
                    investigation
                )

        }