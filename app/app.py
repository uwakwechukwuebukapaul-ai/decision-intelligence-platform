from flask import Flask, jsonify


from app.database.db import engine, Base



# ======================================
# Core Decision Intelligence
# ======================================

from app.routes.autonomous_goal import (
    autonomous_goal_bp
)

from app.routes.autonomous_mission import (
    autonomous_mission_bp
)

from app.routes.strategic_planning import (
    strategic_planning_bp
)

from app.routes.execution_management import (
    execution_management_bp
)

from app.routes.performance_optimization import (
    performance_optimization_bp
)



# ======================================
# Autonomous Intelligence Stack
# ======================================

from app.routes.autonomous_orchestrator import (
    autonomous_orchestrator_bp
)

from app.routes.cognitive_core import (
    cognitive_core_bp
)

from app.routes.autonomous_fabric import (
    autonomous_fabric_bp
)

from app.routes.autonomous_operating_system import (
    autonomous_operating_system_bp
)

from app.routes.collective_operating_intelligence import (
    collective_operating_intelligence_bp
)

from app.routes.collective_intelligence import (
    collective_intelligence_bp
)



# ======================================
# Governance
# ======================================

from app.routes.intelligence_governance import (
    intelligence_governance_bp
)



# ======================================
# Reliability
# ======================================

from app.routes.autonomous_reliability import (
    autonomous_reliability_bp
)



# ======================================
# Self Healing
# ======================================

from app.routes.self_healing_intelligence import (
    self_healing_intelligence_bp
)



# ======================================
# Evolution
# ======================================

from app.routes.autonomous_evolution import (
    autonomous_evolution_bp
)



# ======================================
# Meta Intelligence v9
# ======================================

from app.routes.meta_intelligence import (
    meta_intelligence_bp
)



# ======================================
# Intelligence Control Plane v10
# ======================================

from app.routes.intelligence_control_plane import (
    intelligence_control_plane_bp
)



# ======================================
# Intelligence Memory Fabric v11
# ======================================

from app.routes.intelligence_memory_fabric import (
    intelligence_memory_fabric_bp
)



# ======================================
# Knowledge Graph Intelligence v12
# ======================================

from app.routes.knowledge_graph_intelligence import (
    knowledge_graph_intelligence_bp
)



# ======================================
# Autonomous Reasoning Engine v13
# ======================================

from app.routes.autonomous_reasoning_engine import (
    autonomous_reasoning_engine_bp
)



# ======================================
# Autonomous Decision Core v14
# ======================================

from app.routes.autonomous_decision_core import (
    autonomous_decision_core_bp
)



# ======================================
# Autonomous Agent Workforce v15
# ======================================

from app.routes.autonomous_agent_workforce import (
    autonomous_agent_workforce_bp
)



# ======================================
# Autonomous Learning Engine v16
# ======================================

from app.routes.autonomous_learning_engine import (
    autonomous_learning_engine_bp
)
# ======================================
# Blueprint Registration
# ======================================

def register_blueprints(app):


    # ======================================
    # Core Decision Intelligence
    # ======================================

    app.register_blueprint(
        autonomous_goal_bp
    )

    app.register_blueprint(
        autonomous_mission_bp
    )

    app.register_blueprint(
        strategic_planning_bp
    )

    app.register_blueprint(
        execution_management_bp
    )

    app.register_blueprint(
        performance_optimization_bp
    )



    # ======================================
    # Autonomous Intelligence Stack
    # ======================================

    app.register_blueprint(
        autonomous_orchestrator_bp
    )

    app.register_blueprint(
        cognitive_core_bp
    )

    app.register_blueprint(
        autonomous_fabric_bp
    )

    app.register_blueprint(
        autonomous_operating_system_bp
    )

    app.register_blueprint(
        collective_operating_intelligence_bp
    )

    app.register_blueprint(
        collective_intelligence_bp
    )



    # ======================================
    # Intelligence Governance
    # ======================================

    app.register_blueprint(
        intelligence_governance_bp
    )



    # ======================================
    # Reliability Intelligence
    # ======================================

    app.register_blueprint(
        autonomous_reliability_bp
    )



    # ======================================
    # Self Healing Intelligence
    # ======================================

    app.register_blueprint(
        self_healing_intelligence_bp
    )



    # ======================================
    # Evolution Intelligence
    # ======================================

    app.register_blueprint(
        autonomous_evolution_bp
    )



    # ======================================
    # Meta Intelligence v9
    # ======================================

    app.register_blueprint(
        meta_intelligence_bp
    )



    # ======================================
    # Intelligence Control Plane v10
    # ======================================

    app.register_blueprint(
        intelligence_control_plane_bp
    )



    # ======================================
    # Intelligence Memory Fabric v11
    # ======================================

    app.register_blueprint(
        intelligence_memory_fabric_bp
    )



    # ======================================
    # Knowledge Graph Intelligence v12
    # ======================================

    app.register_blueprint(
        knowledge_graph_intelligence_bp
    )



    # ======================================
    # Autonomous Reasoning Engine v13
    # ======================================

    app.register_blueprint(
        autonomous_reasoning_engine_bp
    )



    # ======================================
    # Autonomous Decision Core v14
    # ======================================

    app.register_blueprint(
        autonomous_decision_core_bp
    )



    # ======================================
    # Autonomous Agent Workforce v15
    # ======================================

    app.register_blueprint(
        autonomous_agent_workforce_bp
    )



    # ======================================
    # Autonomous Learning Engine v16
    # ======================================

    app.register_blueprint(
        autonomous_learning_engine_bp
    )
    # ======================================
# Flask Application Factory
# ======================================

def create_app():

    app = Flask(__name__)


    app.config[
        "JSON_SORT_KEYS"
    ] = False


    register_blueprints(app)


    return app



# ======================================
# Application Instance
# ======================================

app = create_app()



# ======================================
# Root Endpoint
# ======================================

@app.route("/")
def home():

    return jsonify(

        {

            "platform":
                "Decision Intelligence Platform",

            "status":
                "operational",

            "version":
                "16.0"

        }

    )



# ======================================
# Health Endpoint
# ======================================

@app.route("/health")
def health():

    return jsonify(

        {

            "platform":
                "Decision Intelligence Platform",


            "status":
                "healthy",


            "version":
                "16.0",


            "services":

                {


                    "database":
                        "connected",


                    "intelligence_engine":
                        "active",


                    "autonomous_agents":
                        "running",


                    "collective_intelligence":
                        "enabled",


                    "operating_system_layer":
                        "active",


                    "governance_layer":
                        "active",


                    "reliability_layer":
                        "active",


                    "self_healing_layer":
                        "active",


                    "evolution_layer":
                        "active",


                    "meta_intelligence_layer":
                        "active",


                    "control_plane":
                        "active",


                    "memory_fabric":
                        "active",


                    "knowledge_graph":
                        "active",


                    "autonomous_reasoning":
                        "active",


                    "autonomous_decision_core":
                        "active",


                    "autonomous_agent_workforce":
                        "active",


                    "autonomous_learning":
                        "active"

                }

        }

    )



# ======================================
# Development Server
# ======================================

if __name__ == "__main__":


    Base.metadata.create_all(

        bind=engine

    )


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )