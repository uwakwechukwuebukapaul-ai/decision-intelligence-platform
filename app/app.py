from flask import Flask, jsonify
from datetime import datetime


# =====================================
# Database
# =====================================

from app.database.db import engine, Base


# =====================================
# Models
# =====================================

from app.models import *



# =====================================
# Intelligence Fabric
# =====================================

from app.intelligence.production_engine_loader import (
    load_production_engines
)



# =====================================
# Autonomous Intelligence Engines
# =====================================

from app.routes.autonomous_adaptation_engine import autonomous_adaptation_engine
from app.routes.autonomous_agent_workforce import autonomous_agent_workforce
from app.routes.autonomous_decision_core import autonomous_decision_core
from app.routes.autonomous_evolution_engine import autonomous_evolution_engine
from app.routes.autonomous_executive_intelligence_engine import autonomous_executive_intelligence_engine
from app.routes.autonomous_forecasting_engine import autonomous_forecasting_engine
from app.routes.autonomous_governance_engine import autonomous_governance_engine
from app.routes.autonomous_intelligence_fusion_engine import autonomous_intelligence_fusion_engine
from app.routes.autonomous_intelligence_governance_engine import autonomous_intelligence_governance_engine
from app.routes.autonomous_intelligence_orchestrator import autonomous_intelligence_orchestrator
from app.routes.autonomous_intelligence_self_optimization_engine import autonomous_intelligence_self_optimization_engine
from app.routes.autonomous_intelligence_evolution_engine import autonomous_intelligence_evolution_engine
from app.routes.autonomous_cognitive_intelligence_engine import autonomous_cognitive_intelligence_engine
from app.routes.autonomous_knowledge_fabric_engine import autonomous_knowledge_fabric_engine
from app.routes.autonomous_learning_engine import autonomous_learning_engine
from app.routes.autonomous_memory_engine import autonomous_memory_engine
from app.routes.autonomous_meta_intelligence_engine import autonomous_meta_intelligence_engine
from app.routes.autonomous_meta_intelligence_engine_v2 import autonomous_meta_intelligence_engine_v2
from app.routes.autonomous_predictive_intelligence_engine import autonomous_predictive_intelligence_engine
from app.routes.autonomous_reasoning_engine import autonomous_reasoning_engine
from app.routes.autonomous_security_intelligence_engine import autonomous_security_intelligence_engine
from app.routes.autonomous_self_healing_engine import autonomous_self_healing_engine
from app.routes.autonomous_simulation_engine import autonomous_simulation_engine
from app.routes.autonomous_strategic_decision_engine import autonomous_strategic_decision_engine
from app.routes.autonomous_strategic_simulation_engine import autonomous_strategic_simulation_engine
from app.routes.autonomous_trust_intelligence_engine import autonomous_trust_intelligence_engine
from app.routes.autonomous_validation_engine import autonomous_validation_engine



# =====================================
# Platform Modules
# =====================================

from app.routes.autonomous_intelligence_dashboard import autonomous_intelligence_dashboard
from app.routes.autonomous_intelligence_command_center import autonomous_intelligence_command_center
from app.routes.autonomous_intelligence_memory import autonomous_intelligence_memory
from app.routes.autonomous_intelligence_learning import autonomous_intelligence_learning



# =====================================
# Agent Infrastructure
# =====================================

from app.routes.autonomous_operating_system import autonomous_operating_system_bp
from app.routes.agent_runtime import agent_runtime_bp
from app.routes.agent_supervisor import agent_supervisor_bp



# =====================================
# Intelligence Evolution
# =====================================

from app.routes.intelligence_feedback import intelligence_feedback_bp
from app.routes.intelligence_evaluation import intelligence_evaluation_bp
from app.routes.intelligence_reflection import intelligence_reflection_bp
from app.routes.intelligence_orchestration import intelligence_orchestration_bp



# =====================================
# Control Plane
# =====================================

from app.routes.intelligence_control_plane import intelligence_control_plane_bp



# =====================================
# Agent Management
# =====================================

from app.routes.agent_management import agent_management_bp




# =====================================
# Flask Application
# =====================================

app = Flask(__name__)


app.config["PLATFORM_NAME"] = (
    "Decision Intelligence Platform"
)

app.config["VERSION"] = "49.0"



# =====================================
# Database Initialization
# =====================================

Base.metadata.create_all(
    bind=engine
)



# =====================================
# Load Intelligence Capabilities
# =====================================

load_production_engines()



# =====================================
# Blueprint Registry
# =====================================

blueprints = [

    autonomous_adaptation_engine,
    autonomous_agent_workforce,
    autonomous_decision_core,
    autonomous_evolution_engine,
    autonomous_executive_intelligence_engine,
    autonomous_forecasting_engine,
    autonomous_governance_engine,
    autonomous_intelligence_fusion_engine,
    autonomous_intelligence_governance_engine,
    autonomous_intelligence_orchestrator,
    autonomous_intelligence_self_optimization_engine,
    autonomous_intelligence_evolution_engine,
    autonomous_cognitive_intelligence_engine,
    autonomous_knowledge_fabric_engine,
    autonomous_learning_engine,
    autonomous_memory_engine,
    autonomous_meta_intelligence_engine,
    autonomous_meta_intelligence_engine_v2,
    autonomous_predictive_intelligence_engine,
    autonomous_reasoning_engine,
    autonomous_security_intelligence_engine,
    autonomous_self_healing_engine,
    autonomous_simulation_engine,
    autonomous_strategic_decision_engine,
    autonomous_strategic_simulation_engine,
    autonomous_trust_intelligence_engine,
    autonomous_validation_engine,

    autonomous_intelligence_dashboard,
    autonomous_intelligence_command_center,
    autonomous_intelligence_memory,
    autonomous_intelligence_learning,

    autonomous_operating_system_bp,
    agent_runtime_bp,
    agent_supervisor_bp,

    intelligence_feedback_bp,
    intelligence_evaluation_bp,
    intelligence_reflection_bp,
    intelligence_orchestration_bp,

    intelligence_control_plane_bp,

    agent_management_bp
]



for blueprint in blueprints:

    app.register_blueprint(
        blueprint
    )



# =====================================
# Intelligence Fabric Status
# =====================================

@app.route(
    "/intelligence-status",
    methods=["GET"]
)
def intelligence_status():

    from app.intelligence.capability_registry import (
        capability_registry
    )

    return jsonify({

        "platform":
            app.config["PLATFORM_NAME"],

        "version":
            app.config["VERSION"],

        "registered_capabilities":
            capability_registry.list_capabilities(),

        "timestamp":
            datetime.utcnow().isoformat()

    })



# =====================================
# Health Endpoint
# =====================================

@app.route(
    "/health",
    methods=["GET"]
)
def health():

    return jsonify({

        "platform":
            app.config["PLATFORM_NAME"],

        "status":
            "healthy",

        "version":
            app.config["VERSION"],

        "services": {

            "database":
                "active",

            "intelligence_fabric":
                "active",

            "capability_registry":
                "active",

            "autonomous_stack":
                "active",

            "agent_runtime":
                "active",

            "control_plane":
                "active"

        },

        "timestamp":
            datetime.utcnow().isoformat()

    })



# =====================================
# Run Application
# =====================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000
    )