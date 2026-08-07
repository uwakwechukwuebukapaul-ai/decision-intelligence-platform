"""
Sentinel DNA

Application Factory

Responsible for:

- Creating Flask application
- Initializing database
- Starting runtime services
- Loading intelligence engines
- Registering API gateways
"""

from __future__ import annotations

import logging
import os

from flask import Flask


from app.database.db import (
    engine,
    Base
)


from app.intelligence.production_engine_loader import (
    load_production_engines
)


from app.blueprint_registry import (
    register_blueprints
)


from app.health_routes import (
    health_bp
)


from app.core.application import (
    runtime
)


from app.core.lifecycle import (
    lifecycle
)


logger = logging.getLogger(
    "sentinel_dna"
)


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)



def create_app() -> Flask:
    """
    Create Sentinel DNA Flask application.
    """


    app = Flask(
        __name__
    )


    app.config["PLATFORM_NAME"] = os.getenv(
        "PLATFORM_NAME",
        "Sentinel DNA"
    )


    app.config["VERSION"] = os.getenv(
        "PLATFORM_VERSION",
        "50.0"
    )


    app.config["ENVIRONMENT"] = os.getenv(
        "ENVIRONMENT",
        "development"
    )


    logger.info(
        "Starting %s v%s",
        app.config["PLATFORM_NAME"],
        app.config["VERSION"]
    )



    # Database

    Base.metadata.create_all(
        bind=engine
    )


    logger.info(
        "Database initialized"
    )



    # Lifecycle

    lifecycle.startup()


    logger.info(
        "Lifecycle started"
    )



    # Runtime

    runtime.start()


    logger.info(
        "Runtime started"
    )



    # Intelligence Engines

    load_production_engines()


    logger.info(
        "Intelligence engines loaded"
    )



    # API Blueprints

    register_blueprints(
        app
    )


    logger.info(
        "Blueprints registered"
    )



    # Health

    app.register_blueprint(
        health_bp
    )


    logger.info(
        "Health routes registered"
    )



    logger.info(
        "%s ready",
        app.config["PLATFORM_NAME"]
    )


    return app