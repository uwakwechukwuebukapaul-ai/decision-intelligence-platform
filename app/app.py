from flask import Flask
import os


# ===============================
# Database
# ===============================

from app.database.db import engine, Base



# ===============================
# Register Models
# ===============================

from app.models import (
    UserProfile,
    AIReport,
    SkillProgress,
    LearningProgress
)



# ===============================
# Routes
# ===============================

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp
from app.routes.auth import auth_bp
from app.routes.reports import reports_bp
from app.routes.dashboard import dashboard_bp
from app.routes.progress import progress_bp
from app.routes.certification import certification_bp
from app.routes.learning import learning_bp
from app.routes.learning_progress import learning_progress_bp



# ===============================
# AI Intelligence Routes
# ===============================

from app.routes.skill_analysis import skill_analysis_bp
from app.routes.career_report import career_report_bp
from app.routes.decision import decision_bp
from app.routes.recommendation import recommendation_bp
from app.routes.advisor import advisor_bp
from app.routes.mentor import mentor_bp




# ===============================
# Flask Application
# ===============================

app = Flask(

    __name__,

    template_folder=os.path.join(

        os.path.dirname(
            os.path.dirname(__file__)
        ),

        "templates"

    )

)



# ===============================
# Database Initialization
# ===============================

Base.metadata.create_all(

    bind=engine

)




# ===============================
# Core Blueprint Registration
# ===============================


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


app.register_blueprint(
    progress_bp
)


app.register_blueprint(
    certification_bp
)


app.register_blueprint(
    learning_bp
)


app.register_blueprint(
    learning_progress_bp
)




# ===============================
# AI Intelligence Engine Registration
# ===============================


# AI Skill Gap Intelligence

app.register_blueprint(
    skill_analysis_bp
)



# AI Career Intelligence Report

app.register_blueprint(
    career_report_bp
)



# AI Decision Intelligence

app.register_blueprint(
    decision_bp
)



# AI Recommendation Engine

app.register_blueprint(
    recommendation_bp
)



# AI Career Advisor Engine

app.register_blueprint(
    advisor_bp
)



# AI Mentor Engine

app.register_blueprint(
    mentor_bp
)




# ===============================
# Platform Health Endpoint
# ===============================

@app.route("/")

def home():

    return {


        "name":

        "Decision Intelligence Platform",



        "status":

        "running",



        "version":

        "1.5",



        "features":[


            "User Intelligence Profile",


            "AI Decision Engine",


            "Career Matching",


            "AI Reports",


            "AI Mentor",


            "Career Simulation",


            "Career Evolution",


            "Skill Progress Tracking",


            "Certification Intelligence",


            "Learning Roadmap Engine",


            "Adaptive Learning Progress Engine",



            # AI Intelligence Layer


            "AI Skill Gap Intelligence Engine",


            "AI Career Intelligence Report Engine",


            "AI Decision Intelligence Engine v1",


            "AI Career Planner Engine v1",


            "AI Recommendation Engine v1",


            "AI Career Advisor Engine v1",


            "AI Mentor Engine v1"


        ]

    }




# ===============================
# Application Runner
# ===============================

if __name__ == "__main__":


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )