from flask import Blueprint, jsonify


from app.api.api_memory import (
    APIMemory
)



decision_api = Blueprint(
    "decision_api",
    __name__
)



memory = APIMemory()



@decision_api.route(
    "/api/decisions/history",
    methods=["GET"]
)

def decision_history():


    return jsonify(

        memory.history()

    )