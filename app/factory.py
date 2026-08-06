"""
Decision Intelligence Platform

Application Factory
"""

from flask import Flask

from app.database.db import engine, Base

from app.intelligence.production_engine_loader import (
    load_production_engines,
)

from app.blueprint_registry import (
    register_blueprints,
)

from app.health_routes import (
    health_bp,
)

from app.routes.api.v1.intelligence import (
    intelligence_api_bp,
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
    # Platform Lifecycle
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
    # Core Blueprints
    # =====================================

    register_blueprints(app)


    # =====================================
    # Health API
    # =====================================

    app.register_blueprint(
        health_bp
    )


    # =====================================
    # External API Gateway v1
    # =====================================

    app.register_blueprint(
        intelligence_api_bp
    )


    return app