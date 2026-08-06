"""
Decision Intelligence Platform

Application Factory

Central Flask application bootstrap.

Responsibilities:
- Flask initialization
- Blueprint registration
- Runtime wiring
- API exposure
- Enterprise service startup
"""


from __future__ import annotations


from flask import Flask



def create_app():

    """
    Application factory.

    Creates and configures
    the Decision Intelligence Platform.
    """


    app = Flask(
        __name__
    )


    # =====================================
    # Core Configuration
    # =====================================

    app.config.update(

        TESTING=False,

        JSON_SORT_KEYS=False

    )


    # =====================================
    # Register Routes
    # =====================================

    register_routes(
        app
    )


    return app




def register_routes(app):

    """
    Register platform API routes.
    """


    # -------------------------------------
    # Control Plane
    # -------------------------------------

    try:

        from app.routes.control_plane import (
            control_plane_bp
        )

        app.register_blueprint(
            control_plane_bp
        )


    except ImportError:

        pass



    # -------------------------------------
    # Intelligence Fabric
    # -------------------------------------

    try:

        from app.routes.intelligence_execution import (
            intelligence_execution_bp
        )


        app.register_blueprint(
            intelligence_execution_bp
        )


    except ImportError:

        pass



    # -------------------------------------
    # Governance
    # -------------------------------------

    try:

        from app.routes.governance import (
            governance_bp
        )


        app.register_blueprint(
            governance_bp
        )


    except ImportError:

        pass



    # -------------------------------------
    # Health Endpoint
    # -------------------------------------

    @app.get("/health")
    def health():

        return {

            "status":
                "healthy",

            "service":
                "decision-intelligence-platform"

        }, 200