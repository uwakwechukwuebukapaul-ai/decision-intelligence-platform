from flask import Blueprint, jsonify

from app.ai.self_healing_intelligence.healing_controller import (
    HealingController
)

from app.ai.self_healing_intelligence.anomaly_response import (
    AnomalyResponse
)

from app.ai.self_healing_intelligence.repair_engine import (
    RepairEngine
)

from app.ai.self_healing_intelligence.recovery_memory import (
    RecoveryMemory
)

from app.ai.self_healing_intelligence.adaptive_repair import (
    AdaptiveRepair
)

from app.ai.self_healing_intelligence.system_restoration import (
    SystemRestoration
)



self_healing_intelligence_bp = Blueprint(
    "self_healing_intelligence",
    __name__
)



@self_healing_intelligence_bp.route(
    "/self-healing-intelligence/<int:user_id>",
    methods=["GET"]
)
def self_healing_intelligence(user_id):


    controller = HealingController()

    anomaly = AnomalyResponse()

    repair = RepairEngine()

    memory = RecoveryMemory()

    adaptive = AdaptiveRepair()

    restoration = SystemRestoration()



    response = {


        "status":

            "operational",


        "user_id":

            user_id,


        "self_healing_intelligence":

            {


                "healing":

                    controller.evaluate(user_id),


                "anomaly_response":

                    anomaly.analyze(),


                "repair":

                    repair.repair(),


                "recovery_memory":

                    memory.store(),


                "adaptive_repair":

                    adaptive.optimize(),


                "system_restoration":

                    restoration.restore(),


                "overall_healing_score":

                    99,


                "version":

                    "1.0"

            }

    }


    return jsonify(response)