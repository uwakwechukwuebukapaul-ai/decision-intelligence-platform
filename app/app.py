from flask import Flask, jsonify

from app.database.db import engine, Base


# ==============================
# Autonomous Intelligence Layers
# ==============================


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



# ==============================
# Governance Intelligence Layer
# ==============================


from app.routes.intelligence_governance import (
    intelligence_governance_bp
)



# ==============================
# Reliability Intelligence Layer
# ==============================


from app.routes.autonomous_reliability import (
    autonomous_reliability_bp
)



# ==============================
# Self-Healing Intelligence Layer
# ==============================


from app.routes.self_healing_intelligence import (
    self_healing_intelligence_bp
)
def register_blueprints(app):


    # ==============================
    # Autonomous Intelligence Stack
    # ==============================


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



    # ==============================
    # Governance Layer
    # ==============================


    app.register_blueprint(
        intelligence_governance_bp
    )



    # ==============================
    # Reliability Layer
    # ==============================


    app.register_blueprint(
        autonomous_reliability_bp
    )



    # ==============================
    # Self-Healing Layer
    # ==============================


    app.register_blueprint(
        self_healing_intelligence_bp
    )





def create_app():


    app = Flask(__name__)


    app.config[
        "JSON_SORT_KEYS"
    ] = False


    register_blueprints(app)


    return app
app = create_app()



@app.route("/")
def home():

    return jsonify(

        {

            "platform":

                "Decision Intelligence Platform",


            "status":

                "operational",


            "version":

                "7.0"

        }

    )





@app.route("/health")
def health():

    return jsonify(

        {


            "platform":

                "Decision Intelligence Platform",


            "status":

                "healthy",


            "version":

                "7.0",


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

                        "active"


                }

        }

    )





if __name__ == "__main__":


    Base.metadata.create_all(

        bind=engine

    )


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )