"""
Sentinel DNA Report API

Returns AI investigation reports.
"""


from flask import Blueprint, jsonify


from .investigation_api import investigations


from app.ai.reporting import ReportGenerator



report_bp = Blueprint(
    "report_api",
    __name__,
    url_prefix="/api/reports"
)



generator = ReportGenerator()



@report_bp.route(
    "/<investigation_id>",
    methods=["GET"]
)
def get_report(
    investigation_id
):

    investigation = investigations.get(
        investigation_id
    )


    if not investigation:

        return jsonify(
            {
                "error":
                "Investigation not found"
            }
        ), 404



    report = generator.generate(
        investigation
    )


    return jsonify(
        {
            "platform":
                "Sentinel DNA",

            "report":
                report
        }
    )