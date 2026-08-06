"""
Sentinel DNA Analyst Investigation Report

Detailed SOC analyst output.
"""


class AnalystReport:


    def generate(
        self,
        investigation
    ):


        return {

            "investigation":

                investigation.investigation_id,


            "case":

                investigation.case_id,


            "evidence_count":

                len(investigation.evidence),


            "findings":

                investigation.state.findings,


            "risk_score":

                investigation.state.risk_score,


            "agents":

                investigation.state.agents

        }