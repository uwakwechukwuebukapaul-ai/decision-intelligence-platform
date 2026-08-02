from flask import Flask, jsonify
from flask_cors import CORS


# ==================================================
# Route Imports
# ==================================================

from app.routes.autonomous_reasoning_engine import (
    autonomous_reasoning_engine
)

from app.routes.autonomous_decision_core import (
    autonomous_decision_core
)

from app.routes.autonomous_agent_workforce import (
    autonomous_agent_workforce
)

from app.routes.autonomous_learning_engine import (
    autonomous_learning_engine
)

from app.routes.autonomous_adaptation_engine import (
    autonomous_adaptation_engine
)

from app.routes.autonomous_evolution_engine import (
    autonomous_evolution_engine
)

from app.routes.autonomous_intelligence_orchestrator import (
    autonomous_intelligence_orchestrator
)

from app.routes.autonomous_memory_engine import (
    autonomous_memory_engine
)

from app.routes.autonomous_knowledge_fabric_engine import (
    autonomous_knowledge_fabric_engine
)



# ==================================================
# Application Factory
# ==================================================

def create_app():

    app = Flask(__name__)


    CORS(app)


    app.config["JSON_SORT_KEYS"] = False



    # ==================================================
    # Blueprint Registration
    # ==================================================

    app.register_blueprint(
        autonomous_reasoning_engine
    )


    app.register_blueprint(
        autonomous_decision_core
    )


    app.register_blueprint(
        autonomous_agent_workforce
    )


    app.register_blueprint(
        autonomous_learning_engine
    )


    app.register_blueprint(
        autonomous_adaptation_engine
    )


    app.register_blueprint(
        autonomous_evolution_engine
    )


    app.register_blueprint(
        autonomous_intelligence_orchestrator
    )


    app.register_blueprint(
        autonomous_memory_engine
    )


    app.register_blueprint(
        autonomous_knowledge_fabric_engine
    )



    # ==================================================
    # Platform Health
    # ==================================================

    @app.route(
        "/health",
        methods=["GET"]
    )

    def health():

        return jsonify({

            "platform":
                "Decision Intelligence Platform",


            "status":
                "healthy",


            "version":
                "21.0",



            "services": {


                "autonomous_reasoning":
                    "active",


                "autonomous_decision_core":
                    "active",


                "autonomous_agent_workforce":
                    "active",


                "autonomous_learning":
                    "active",


                "autonomous_adaptation":
                    "active",


                "autonomous_evolution":
                    "active",


                "autonomous_intelligence_orchestrator":
                    "active",


                "autonomous_memory_engine":
                    "active",


                "autonomous_knowledge_fabric_engine":
                    "active",


                "autonomous_agents":
                    "running",


                "collective_intelligence":
                    "enabled",


                "control_plane":
                    "active",


                "database":
                    "connected",


                "governance_layer":
                    "active",


                "intelligence_engine":
                    "active",


                "knowledge_graph":
                    "active",


                "memory_fabric":
                    "active",


                "meta_intelligence_layer":
                    "active",


                "operating_system_layer":
                    "active",


                "reliability_layer":
                    "active",


                "self_healing_layer":
                    "active"

            }

        })



    # ==================================================
    # Error Handlers
    # ==================================================

    @app.errorhandler(404)

    def not_found(error):

        return jsonify({

            "status":
                "error",

            "message":
                "Endpoint not found"

        }), 404



    @app.errorhandler(500)

    def internal_error(error):

        return jsonify({

            "status":
                "error",

            "message":
                "Internal server error"

        }), 500



    return app




# ==================================================
# Flask Instance
# ==================================================

app = create_app()



# ==================================================
# Development Server
# ==================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )