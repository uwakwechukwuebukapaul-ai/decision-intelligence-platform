from flask import Blueprint, jsonify
from datetime import datetime



health_api = Blueprint(
    "health_api",
    __name__
)



@health_api.route(
    "/api/health",
    methods=["GET"]
)

def health_check():


    return jsonify(

        {

            "platform":
                "Decision Intelligence Platform",


            "status":
                "healthy",


            "api_gateway":
                "active",


            "timestamp":
                datetime.utcnow().isoformat()

        }

    )