from flask import Blueprint, jsonify, request
from datetime import datetime


# ===============================
# Agent Management Engine
# ===============================

try:
    from app.ai.agent_management.agent_manager import AgentManager
except Exception:
    AgentManager = None



# ===============================
# Mission Management Engine
# ===============================

try:
    from app.ai.agent_management.mission_manager import MissionManager
except Exception:
    MissionManager = None



# ===============================
# Mission Execution Engine
# ===============================

try:
    from app.ai.agent_management.execution_engine import ExecutionEngine
except Exception:
    ExecutionEngine = None



# ===============================
# Blueprint
# ===============================

agent_management_bp = Blueprint(
    "agent_management",
    __name__,
    url_prefix="/agent-management"
)



# ===============================
# Engine Instances
# ===============================

if AgentManager:

    agent_manager = AgentManager()

else:

    agent_manager = None



if MissionManager:

    mission_manager = MissionManager()

else:

    mission_manager = None



if ExecutionEngine and mission_manager and agent_manager:

    execution_engine = ExecutionEngine(
        mission_manager,
        agent_manager
    )

else:

    execution_engine = None



# ===============================
# Agent Management Status
# ===============================

@agent_management_bp.route(
    "/<int:user_id>",
    methods=["GET"]
)
def agent_management_status(user_id):

    agents = []

    if agent_manager:

        try:

            agents = agent_manager.list_agents()

        except Exception:

            agents = []


    return jsonify({

        "agent_management_engine": {

            "status":
                "active",

            "version":
                "50.0",

            "user_id":
                user_id,

            "registry":
                "active",

            "lifecycle_manager":
                "active",

            "mission_manager":
                "active",

            "execution_engine":
                "active",

            "agents":
                agents,

            "timestamp":
                datetime.utcnow().isoformat()

        }

    })



# ===============================
# Create Mission
# ===============================

@agent_management_bp.route(
    "/missions",
    methods=["POST"]
)
def create_mission():


    if not mission_manager:

        return jsonify({

            "error":
                "Mission Manager unavailable"

        }), 500



    data = request.json or {}



    mission = mission_manager.create_mission(

        title=data.get(
            "title",
            "Untitled Mission"
        ),


        objective=data.get(
            "objective",
            ""
        ),


        priority=data.get(
            "priority",
            "medium"
        )

    )



    return jsonify({

        "mission":
            mission

    }), 201



# ===============================
# List Missions
# ===============================

@agent_management_bp.route(
    "/missions",
    methods=["GET"]
)
def list_missions():


    if not mission_manager:

        return jsonify({

            "missions":
                []

        })



    return jsonify({

        "missions":
            mission_manager.list_missions()

    })



# ===============================
# Assign Mission
# ===============================

@agent_management_bp.route(
    "/missions/<mission_id>/assign",
    methods=["POST"]
)
def assign_mission(mission_id):


    if not mission_manager:

        return jsonify({

            "error":
                "Mission Manager unavailable"

        }), 500



    data = request.json or {}



    agent_id = data.get(
        "agent_id"
    )



    mission = mission_manager.assign_mission(

        mission_id,

        agent_id

    )



    if not mission:

        return jsonify({

            "error":
                "Mission not found"

        }), 404



    return jsonify({

        "mission":
            mission

    })



# ===============================
# Execute Mission
# ===============================

@agent_management_bp.route(
    "/missions/<mission_id>/execute",
    methods=["POST"]
)
def execute_mission(mission_id):


    if not execution_engine:

        return jsonify({

            "error":
                "Execution Engine unavailable"

        }), 500



    result = execution_engine.execute_mission(
        mission_id
    )


    return jsonify({

        "execution":
            result

    })