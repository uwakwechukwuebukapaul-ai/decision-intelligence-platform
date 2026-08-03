from flask import Blueprint, jsonify, request


from app.dashboard.decision_dashboard import (
    DecisionDashboard
)



decision_api = Blueprint(
    "decision_api",
    __name__
)



dashboard = DecisionDashboard()



@decision_api.route(
    "/dashboard/decision",
    methods=["POST"]
)

def create_dashboard():

    data = request.json


    result = dashboard.display(
        data
    )


    return jsonify(result)



@decision_api.route(
    "/dashboard/history",
    methods=["GET"]
)

def dashboard_history():


    return jsonify(
        dashboard.history()
    )