from flask import Blueprint, jsonify

from app.database.db import SessionLocal
from app.models.report import AIReport


reports_bp = Blueprint(
    "reports",
    __name__
)


@reports_bp.route(
    "/reports/<int:user_id>",
    methods=["GET"]
)
def get_reports(user_id):

    db = SessionLocal()

    reports = db.query(AIReport).filter(
        AIReport.user_id == user_id
    ).all()


    db.close()


    return jsonify({

        "user_id": user_id,

        "total_reports": len(reports),

        "reports": [

            {
                "id": report.id,

                "content": report.report_content

            }

            for report in reports

        ]

    })