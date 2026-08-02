from flask import Blueprint, jsonify

from app.ai.autonomous_intelligence_dashboard import (
    DashboardController
)


autonomous_intelligence_dashboard = Blueprint(
    "autonomous_intelligence_dashboard",
    __name__
)


@autonomous_intelligence_dashboard.route(
    "/autonomous-intelligence-dashboard/<int:user_id>",
    methods=["GET"]
)
def autonomous_intelligence_dashboard_route(user_id):

    controller = DashboardController(
        user_id
    )

    result = controller.generate_dashboard()


    return jsonify({

        "status": "operational",

        "user_id": user_id,

        "autonomous_intelligence_dashboard": result

    })