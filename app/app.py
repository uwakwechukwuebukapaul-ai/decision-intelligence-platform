from flask import Flask

from app.database.db import engine, Base

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp
from app.routes.auth import auth_bp


app = Flask(__name__)


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


@app.route("/")
def home():

    return {

        "name": "Decision Intelligence Platform",

        "status": "running",

        "version": "0.2",

        "features": [

            "User Profile System",

            "AI Decision Engine",

            "Career Matching",

            "LLM Reasoning",

            "Authentication System"

        ]

    }