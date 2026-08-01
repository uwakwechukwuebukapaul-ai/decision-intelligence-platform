from flask import Flask
import os

from app.database.db import engine, Base

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp
from app.routes.auth import auth_bp
from app.routes.reports import reports_bp
from app.routes.dashboard import dashboard_bp
from app.routes.skills import skills_bp



app = Flask(

    __name__,

    template_folder=os.path.join(

        os.path.dirname(
            os.path.dirname(__file__)
        ),

        "templates"

    )

)



# =====================================
# Database Initialization
# =====================================


Base.metadata.create_all(

    bind=engine

)





# =====================================
# Register Application Routes
# =====================================



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



# AI Skill Progress Tracking v18

app.register_blueprint(

    skills_bp

)







# =====================================
# Health Check Endpoint
# =====================================


@app.route("/")
def home():


    return {


        "name":

        "Decision Intelligence Platform",



        "status":

        "running",



        "version":

        "0.6",



        "features": [


            "User Profile System",


            "AI Decision Engine",


            "Career Matching",


            "LLM Reasoning",


            "Authentication System",


            "AI Report History",


            "Intelligence Dashboard",


            "AI Mentor Intelligence",


            "Career Readiness Tracking",


            "Career Evolution Engine",


            "Career Simulation Engine",


            "AI Learning Intelligence",


            "Skill Progress Tracking API"


        ]

    }





if __name__ == "__main__":


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )