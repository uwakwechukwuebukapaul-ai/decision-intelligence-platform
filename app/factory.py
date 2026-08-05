"""
Decision Intelligence Platform

Application Factory
"""

from flask import Flask

from app.database.db import engine, Base

from app.intelligence.production_engine_loader import (
    load_production_engines
)

from app.blueprint_registry import (
    register_blueprints
)

from app.health_routes import (
    health_bp
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
        "49.0"
    )


    # =====================================
    # Database Initialization
    # =====================================

    Base.metadata.create_all(
        bind=engine
    )


    # =====================================
    # Intelligence Fabric Initialization
    # =====================================

    load_production_engines()


    # =====================================
    # Register Application Routes
    # =====================================

    register_blueprints(app)


    app.register_blueprint(
        health_bp
    )


    return app