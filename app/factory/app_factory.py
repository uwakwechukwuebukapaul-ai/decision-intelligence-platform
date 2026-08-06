from flask import Flask


def create_app():

    app = Flask(
        __name__
    )


    from app.api.control_plane import (
        control_plane_bp
    )

    from app.api.intelligence import (
        intelligence_bp
    )


    app.register_blueprint(
        control_plane_bp
    )


    app.register_blueprint(
        intelligence_bp
    )


    return app