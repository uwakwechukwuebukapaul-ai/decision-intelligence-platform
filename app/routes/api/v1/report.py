"""
Sentinel DNA - Investigation Report API

Provides analyst access to generated IOC investigation reports.
"""

from flask import Blueprint, jsonify

from app.intelligence.ioc.fusion import IntelligenceFusion

from app.intelligence.reporting import ReportGenerator

report_api_bp = Blueprint(
    "report_api",
    __name__,
    url_prefix="/api/v1/report",
)


fusion_engine = IntelligenceFusion()
report_engine = ReportGenerator()


@report_api_bp.route(
    "/ioc/<indicator>",
    methods=["GET"],
)
def generate_ioc_report(indicator: str):

    intelligence = fusion_engine.analyze(
        indicator
    )


    report = report_engine.generate(
        intelligence
    )


    return jsonify(
        {
            "service": "sentinel-dna-reporting",
            "indicator": indicator,
            "report": report,
        }
    )