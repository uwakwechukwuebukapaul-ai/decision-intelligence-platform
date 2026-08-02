from flask import Blueprint, jsonify

from app.ai.autonomous_security_intelligence_engine import (
    SecurityController
)



autonomous_security_intelligence_engine = Blueprint(
    "autonomous_security_intelligence_engine",
    __name__
)



@autonomous_security_intelligence_engine.route(
    "/autonomous-security-intelligence-engine/<int:user_id>",
    methods=["GET"]
)
def autonomous_security_intelligence(user_id):


    controller = SecurityController(
        user_id
    )


    result = controller.execute_security_cycle()


    return jsonify({

        "status": "operational",

        "user_id": user_id,

        "autonomous_security_intelligence_engine": result

    })