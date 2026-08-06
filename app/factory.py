"""
Decision Intelligence Platform

Application Factory

Responsible for:
- Creating Flask application
- Initializing database
- Starting runtime services
- Loading intelligence engines
- Registering API gateways
"""

from __future__ import annotations


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




def create_app() -> Flask:
    """
    Application factory.
    """


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
    # API Blueprint Registry
    # =====================================

    register_blueprints(
        app
    )



    # =====================================
    # Health Routes
    # =====================================

    app.register_blueprint(
        health_bp
    )



    return app