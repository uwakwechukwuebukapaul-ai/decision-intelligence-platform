from flask import Flask

from app.database.db import engine, Base

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp



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



@app.route("/")
def home():

    return {

        "name": "Decision Intelligence Platform",

        "status": "running",

        "version": "0.1"

    }