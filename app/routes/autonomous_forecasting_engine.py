from flask import Blueprint, jsonify

from app.ai.autonomous_forecasting_engine import (
    ForecastController
)


autonomous_forecasting_engine = Blueprint(
    "autonomous_forecasting_engine",
    __name__
)


@autonomous_forecasting_engine.route(
    "/autonomous-forecasting-engine/<int:user_id>",
    methods=["GET"]
)
def autonomous_forecasting(user_id):

    controller = ForecastController(
        user_id
    )

    result = controller.execute_forecast_cycle()

    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "autonomous_forecasting_engine":
            result

    })