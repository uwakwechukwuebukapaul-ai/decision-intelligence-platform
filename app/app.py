from flask import Flask, jsonify
import os


# =====================================================
# Database
# =====================================================

from app.database.db import engine, Base


# =====================================================
# Models Registration
# =====================================================

from app.models import (
    UserProfile,
    AIReport,
    SkillProgress,
    LearningProgress
)


# =====================================================
# Existing Routes
# =====================================================

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp
from app.routes.auth import auth_bp


from app.routes.autonomous_reasoning_engine import (
    autonomous_reasoning_engine
)

from app.routes.autonomous_decision_core import (
    autonomous_decision_core
)

from app.routes.autonomous_learning_engine import (
    autonomous_learning_engine
)

from app.routes.autonomous_agent_workforce import (
    autonomous_agent_workforce
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


# =====================================================
# NEW v26 ENGINE
# =====================================================

from app.routes.autonomous_security_intelligence_engine import (
    autonomous_security_intelligence_engine
)



# =====================================================
# Application Factory
# =====================================================

def create_app():

    app = Flask(__name__)


    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "decision-intelligence-secret"
    )


    # =================================================
    # Core Routes
    # =================================================

    app.register_blueprint(profile_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(auth_bp)


    # =================================================
    # Autonomous Intelligence Stack
    # =================================================

    app.register_blueprint(
        autonomous_reasoning_engine
    )

    app.register_blueprint(
        autonomous_decision_core
    )

    app.register_blueprint(
        autonomous_learning_engine
    )

    app.register_blueprint(
        autonomous_agent_workforce
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


    # =================================================
    # v26 Security Intelligence Layer
    # =================================================

    app.register_blueprint(
        autonomous_security_intelligence_engine
    )


    # =================================================
    # Health Endpoint
    # =================================================

    @app.route("/health")
    def health():

        return jsonify({

            "platform":
            "Decision Intelligence Platform",

            "status":
            "healthy",

            "version":
            "26.0",

            "services": {

                "database":
                "connected",

                "autonomous_reasoning":
                "active",

                "autonomous_decision_core":
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

                "autonomous_security_intelligence_engine":
                "active"

            }

        })


    return app



# =====================================================
# Application Instance
# =====================================================

app = create_app()