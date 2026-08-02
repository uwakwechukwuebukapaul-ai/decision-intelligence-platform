from flask import Flask, jsonify
from flask_cors import CORS


# ===============================
# Database
# ===============================

from app.database.db import engine, Base


# ===============================
# Import Models
# ===============================

from app.models import *


# ===============================
# Routes
# ===============================

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

from app.routes.autonomous_self_healing_engine import (
    autonomous_self_healing_engine
)

from app.routes.autonomous_governance_engine import (
    autonomous_governance_engine
)

from app.routes.autonomous_meta_intelligence_engine import (
    autonomous_meta_intelligence_engine
)

from app.routes.autonomous_trust_intelligence_engine import (
    autonomous_trust_intelligence_engine
)


# ===============================
# Application Factory
# ===============================

def create_app():

    app = Flask(__name__)


    CORS(app)


    app.config["JSON_SORT_KEYS"] = False



    # ===============================
    # Register Blueprints
    # ===============================

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

    app.register_blueprint(
        autonomous_self_healing_engine
    )

    app.register_blueprint(
        autonomous_governance_engine
    )

    app.register_blueprint(
        autonomous_meta_intelligence_engine
    )

    app.register_blueprint(
        autonomous_trust_intelligence_engine
    )


    # ===============================
    # Health Endpoint
    # ===============================

    @app.route("/health")
    def health():

        return jsonify({

            "platform":
                "Decision Intelligence Platform",


            "status":
                "healthy",


            "version":
                "25.0",


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


                "autonomous_self_healing_engine":
                    "active",


                "autonomous_governance_engine":
                    "active",


                "autonomous_meta_intelligence_engine":
                    "active",


                "autonomous_trust_intelligence_engine":
                    "active",


                "database":
                    "connected",


                "knowledge_graph":
                    "active",


                "memory_fabric":
                    "active",


                "meta_intelligence_layer":
                    "active",


                "governance_layer":
                    "active",


                "self_healing_layer":
                    "active"

            }

        })


    return app



# ===============================
# Application Entry
# ===============================

app = create_app()



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )