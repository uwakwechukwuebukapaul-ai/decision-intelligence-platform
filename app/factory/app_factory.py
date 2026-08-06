"""
Decision Intelligence Platform

Application Factory

Responsible for:
- Flask application creation
- Database initialization
- Runtime startup
- Intelligence engine loading
- Blueprint registration
"""

from flask import Flask


from app.database.db import (
    engine,
    Base,
)


from app.intelligence.production_engine_loader import (
    load_production_engines,
)


from app.blueprint_registry import (
    register_blueprints,
)


from app.health_routes import (
    health_bp,
)


from app.core.application import (
    runtime,
)


from app.core.lifecycle import (
    lifecycle,
)



def create_app():

    app = Flask(__name__)


    # =====================================
    # Configuration
    # =====================================

    app.config["PLATFORM_NAME"] = (
        "Decision Intelligence Platform"
    )

    app.config["VERSION"] = (
        "50.0"
    )


    # =====================================
    # Database
    # =====================================

    Base.metadata.create_all(
        bind=engine
    )


    # =====================================
    # Lifecycle
    # =====================================

    lifecycle.startup()


    # =====================================
    # Runtime
    # =====================================

    runtime.start()


    # =====================================
    # Intelligence Engines
    # =====================================

    load_production_engines()


    # =====================================
    # Blueprint Registration
    # =====================================

    register_blueprints(
        app
    )


    # =====================================
    # Health Endpoint
    # =====================================

    app.register_blueprint(
        health_bp
    )


    return app