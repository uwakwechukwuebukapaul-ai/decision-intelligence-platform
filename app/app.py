from flask import Flask
import os

from app.database.db import engine, Base

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp
from app.routes.auth import auth_bp
from app.routes.reports import reports_bp
from app.routes.dashboard import dashboard_bp


app = Flask(
    __name__,
    template_folder=os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "templates"
    )
)


# Create database tables

Base.metadata.create_all(
    bind=engine
)


# Register API routes

app.register_blueprint(
    profile_bp
)


app.register_blueprint(
    analysis_bp
)


app.register_blueprint(
    auth_bp
)


app.register_blueprint(
    reports_bp
)


app.register_blueprint(
    dashboard_bp
)


@app.route("/")
def home():

    return {

        "name": "Decision Intelligence Platform",

        "status": "running",

        "version": "0.5",

        "features": [

            "User Profile System",

            "AI Decision Engine",

            "Career Matching",

            "LLM Reasoning",

            "Authentication System",

            "AI Report History",

            "Intelligence Dashboard"

        ]

    }