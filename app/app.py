from flask import Flask
import os


# =====================================================
# Database
# =====================================================

from app.database.db import engine, Base



# =====================================================
# Register Models
# =====================================================

from app.models import (
    UserProfile,
    AIReport,
    SkillProgress,
    LearningProgress
)



# =====================================================
# Core Routes
# =====================================================

from app.routes.profile import profile_bp
from app.routes.analysis import analysis_bp
from app.routes.auth import auth_bp
from app.routes.reports import reports_bp
from app.routes.dashboard import dashboard_bp
from app.routes.progress import progress_bp
from app.routes.certification import certification_bp
from app.routes.learning import learning_bp
from app.routes.learning_progress import learning_progress_bp



# =====================================================
# AI Intelligence Routes
# =====================================================

from app.routes.skill_analysis import skill_analysis_bp
from app.routes.career_report import career_report_bp
from app.routes.decision import decision_bp
from app.routes.recommendation import recommendation_bp
from app.routes.advisor import advisor_bp
from app.routes.mentor import mentor_bp
from app.routes.coach import coach_bp
from app.routes.intelligence import intelligence_bp



# =====================================================
# Advanced AI Simulation Routes
# =====================================================

from app.routes.digital_twin import digital_twin_bp
from app.routes.career_simulation import career_simulation_bp
from app.routes.career_evolution import career_evolution_bp



# =====================================================
# AI Memory Routes
# =====================================================

from app.routes.memory import memory_bp



# =====================================================
# AI Knowledge Graph Routes
# =====================================================

from app.routes.intelligence_graph import intelligence_graph_bp



# =====================================================
# AI Reasoning Routes
# =====================================================

from app.routes.decision_reasoning import decision_reasoning_bp



# =====================================================
# AI Orchestration Routes
# =====================================================

from app.routes.decision_orchestrator import decision_orchestrator_bp



# =====================================================
# AI Agent Runtime Routes
# =====================================================

from app.routes.agent_runtime import agent_runtime_bp



# =====================================================
# AI Agent Tools Routes
# =====================================================

from app.routes.agent_tools import agent_tools_bp



# =====================================================
# AI Agent Planner Routes
# =====================================================

from app.routes.agent_planner import agent_planner_bp



# =====================================================
# AI Agent Supervisor Routes
# =====================================================

from app.routes.agent_supervisor import agent_supervisor_bp



# =====================================================
# AI Agent Memory Routes
# =====================================================

from app.routes.agent_memory import agent_memory_bp




# =====================================================
# Application Metadata
# =====================================================

APP_NAME = "Decision Intelligence Platform"

APP_VERSION = "2.8"

APP_STATUS = "running"




# =====================================================
# Flask Application
# =====================================================

app = Flask(

    __name__,

    template_folder=os.path.join(

        os.path.dirname(
            os.path.dirname(__file__)
        ),

        "templates"

    )

)




# =====================================================
# Database Initialization
# =====================================================

Base.metadata.create_all(

    bind=engine

)




# =====================================================
# Blueprint Registry
# =====================================================

BLUEPRINTS = [


    # Core Platform

    profile_bp,
    analysis_bp,
    auth_bp,
    reports_bp,
    dashboard_bp,
    progress_bp,
    certification_bp,
    learning_bp,
    learning_progress_bp,



    # AI Intelligence Layer

    skill_analysis_bp,
    career_report_bp,
    decision_bp,
    recommendation_bp,
    advisor_bp,
    mentor_bp,
    coach_bp,
    intelligence_bp,



    # AI Simulation Layer

    digital_twin_bp,
    career_simulation_bp,
    career_evolution_bp,



    # AI Memory Layer

    memory_bp,



    # AI Knowledge Layer

    intelligence_graph_bp,



    # AI Reasoning Layer

    decision_reasoning_bp,



    # AI Orchestration Layer

    decision_orchestrator_bp,



    # AI Agent Layer

    agent_runtime_bp,
    agent_tools_bp,
    agent_planner_bp,
    agent_supervisor_bp,
    agent_memory_bp

]




# =====================================================
# Register Blueprints
# =====================================================

for blueprint in BLUEPRINTS:

    app.register_blueprint(

        blueprint

    )




# =====================================================
# Root Endpoint
# =====================================================

@app.route("/")

def home():

    return {


        "name":

            APP_NAME,


        "status":

            APP_STATUS,


        "version":

            APP_VERSION,


        "architecture":

            "AI Decision Intelligence Platform",



        "engines":[


            "User Intelligence Profile Engine",

            "Decision Intelligence Engine",

            "Career Matching Engine",

            "AI Report Engine",

            "AI Mentor Engine",

            "AI Career Simulation Engine",

            "AI Career Evolution Engine",

            "Skill Progress Engine",

            "Certification Intelligence Engine",

            "Learning Roadmap Engine",

            "Adaptive Learning Engine",



            "AI Skill Gap Intelligence Engine",

            "AI Career Intelligence Report Engine",

            "AI Recommendation Engine",

            "AI Career Advisor Engine",

            "AI Cybersecurity Coach Engine",

            "AI User Intelligence Profile v2",



            "AI Digital Twin Engine v1",

            "AI Career Simulation Engine v1",

            "AI Career Evolution Engine v1",



            "AI Decision Memory Engine v1",

            "AI Intelligence Graph Engine v1",

            "AI Decision Reasoning Engine v1",

            "AI Decision Orchestrator Engine v1",



            "AI Agent Runtime Engine v1",

            "AI Agent Tool Execution Engine v1",

            "AI Agent Planner Engine v1",

            "AI Agent Supervisor Engine v1",

            "AI Agent Memory Engine v1"


        ],



        "blueprints_loaded":

            len(BLUEPRINTS)

    }




# =====================================================
# Health Endpoint
# =====================================================

@app.route("/health")

def health():

    return {


        "application":

            APP_NAME,


        "status":

            "healthy",


        "database":

            "connected",


        "api":

            "operational",


        "version":

            APP_VERSION,


        "blueprints":

            len(BLUEPRINTS)

    }




# =====================================================
# Platform Information
# =====================================================

@app.route("/api/info")

def platform_info():

    return {


        "platform":

            APP_NAME,


        "version":

            APP_VERSION,


        "modules":[


            "Decision Intelligence",

            "Career Intelligence",

            "AI Mentor",

            "Cybersecurity Coach",

            "User Intelligence",

            "Learning Intelligence",

            "Digital Twin Simulation",

            "Career Simulation Intelligence",

            "Career Evolution Intelligence",

            "Decision Memory Intelligence",

            "Intelligence Graph Reasoning",

            "Decision Reasoning Intelligence",

            "Decision Orchestration Intelligence",

            "Agent Runtime Intelligence",

            "Agent Tool Execution Intelligence",

            "Agent Planning Intelligence",

            "Agent Supervisor Intelligence",

            "Agent Memory Intelligence"


        ]

    }




# =====================================================
# Runner
# =====================================================

if __name__ == "__main__":


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )