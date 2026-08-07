"""
Investigation Report Generator
"""


from .report_schema import (
    create_report,
)



class ReportGenerator:
    """
    Creates analyst-ready reports.
    """


    def generate(
        self,
        case_id,
        assessment,
        intelligence_results,
    ):


        findings = []


        for result in intelligence_results:

            findings.append(

                {

                    "capability":
                        result.get(
                            "capability"
                        ),

                    "result":
                        result.get(
                            "result"
                        ),

                }

            )


        recommendations = self.generate_recommendations(
            assessment
        )


        return create_report(

            case_id,

            assessment,

            findings,

            recommendations,

        )


    def generate_recommendations(
        self,
        assessment,
    ):


        if assessment.get(
            "verdict"
        ) == "malicious":

            return [

                "Investigate affected assets",

                "Review indicators of compromise",

                "Initiate incident response workflow",

            ]


        return [

            "Continue monitoring"

        ]