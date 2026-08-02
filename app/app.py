from flask import Flask, jsonify

from app.database.db import engine, Base


# ======================================
# Core Decision Intelligence Routes
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



# ======================================
# Collective Intelligence
# ======================================

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
# Meta Intelligence
# ======================================

from app.routes.meta_intelligence import (
    meta_intelligence_bp
)



# ======================================
# Intelligence Control Plane
# ======================================

from app.routes.intelligence_control_plane import (
    intelligence_control_plane_bp
)



# ======================================
# Intelligence Memory Fabric
# ======================================

from app.routes.intelligence_memory_fabric import (
    intelligence_memory_fabric_bp
)



# ======================================
# Knowledge Graph Intelligence
# ======================================

from app.routes.knowledge_graph_intelligence import (
    knowledge_graph_intelligence_bp
)



# ======================================
# Autonomous Reasoning Engine
# ======================================

from app.routes.autonomous_reasoning_engine import (
    autonomous_reasoning_engine_bp
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



    # ======================================
    # Collective Intelligence Layer
    # ======================================

    app.register_blueprint(
        collective_operating_intelligence_bp
    )


    app.register_blueprint(
        collective_intelligence_bp
    )



    # ======================================
    # Governance Layer
    # ======================================

    app.register_blueprint(
        intelligence_governance_bp
    )



    # ======================================
    # Reliability Layer
    # ======================================

    app.register_blueprint(
        autonomous_reliability_bp
    )



    # ======================================
    # Self Healing Layer
    # ======================================

    app.register_blueprint(
        self_healing_intelligence_bp
    )



    # ======================================
    # Evolution Layer
    # ======================================

    app.register_blueprint(
        autonomous_evolution_bp
    )



    # ======================================
    # Meta Intelligence Layer
    # ======================================

    app.register_blueprint(
        meta_intelligence_bp
    )



    # ======================================
    # Intelligence Control Plane Layer
    # ======================================

    app.register_blueprint(
        intelligence_control_plane_bp
    )



    # ======================================
    # Intelligence Memory Fabric Layer
    # ======================================

    app.register_blueprint(
        intelligence_memory_fabric_bp
    )



    # ======================================
    # Knowledge Graph Intelligence Layer
    # ======================================

    app.register_blueprint(
        knowledge_graph_intelligence_bp
    )



    # ======================================
    # Autonomous Reasoning Engine Layer
    # ======================================

    app.register_blueprint(
        autonomous_reasoning_engine_bp
    )
  # ======================================
# Flask Application Factory
# ======================================

def create_app():

    app = Flask(__name__)


    app.config["JSON_SORT_KEYS"] = False


    register_blueprints(app)


    return app



# ======================================
# Flask Application Instance
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
                "13.0"

        }

    )



# ======================================
# Health Monitoring Endpoint
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
                "13.0",


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
                        "active"

                }

        }

    )



# ======================================
# Development Runner
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