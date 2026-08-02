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
# Simulation Routes
# =====================================================

from app.routes.digital_twin import digital_twin_bp
from app.routes.career_simulation import career_simulation_bp
from app.routes.career_evolution import career_evolution_bp



# =====================================================
# Memory Routes
# =====================================================

from app.routes.memory import memory_bp
from app.routes.memory_consolidation import memory_consolidation_bp



# =====================================================
# Knowledge Graph Routes
# =====================================================

from app.routes.intelligence_graph import intelligence_graph_bp



# =====================================================
# Reasoning Routes
# =====================================================

from app.routes.decision_reasoning import decision_reasoning_bp



# =====================================================
# Orchestration Routes
# =====================================================

from app.routes.decision_orchestrator import decision_orchestrator_bp



# =====================================================
# Autonomous Agent Routes
# =====================================================

from app.routes.agent_runtime import agent_runtime_bp
from app.routes.agent_tools import agent_tools_bp
from app.routes.agent_planner import agent_planner_bp
from app.routes.agent_supervisor import agent_supervisor_bp
from app.routes.agent_memory import agent_memory_bp
from app.routes.agent_learning import agent_learning_bp
from app.routes.agent_loop import agent_loop_bp



# =====================================================
# Multi Agent Routes
# =====================================================

from app.routes.multi_agent import multi_agent_bp



# =====================================================
# Agent Communication Routes
# =====================================================

from app.routes.agent_communication import agent_communication_bp



# =====================================================
# Agent Governance Routes
# =====================================================

from app.routes.agent_governance import agent_governance_bp



# =====================================================
# Agent Reflection Routes
# =====================================================

from app.routes.agent_reflection import agent_reflection_bp



# =====================================================
# Agent Adaptation Routes
# =====================================================

from app.routes.agent_adaptation import agent_adaptation_bp



# =====================================================
# Agent Evolution Routes
# =====================================================

from app.routes.agent_evolution import agent_evolution_bp




# =====================================================
# Application Metadata
# =====================================================

APP_NAME = "Decision Intelligence Platform"

APP_VERSION = "3.7"

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



    # Simulation Layer

    digital_twin_bp,
    career_simulation_bp,
    career_evolution_bp,



    # Memory Layer

    memory_bp,
    memory_consolidation_bp,



    # Knowledge Layer

    intelligence_graph_bp,



    # Reasoning Layer

    decision_reasoning_bp,



    # Orchestration Layer

    decision_orchestrator_bp,



    # Autonomous Agent Layer

    agent_runtime_bp,
    agent_tools_bp,
    agent_planner_bp,
    agent_supervisor_bp,
    agent_memory_bp,
    agent_learning_bp,
    agent_loop_bp,



    # Multi Agent Layer

    multi_agent_bp,



    # Communication Layer

    agent_communication_bp,



    # Governance Layer

    agent_governance_bp,



    # Reflection Layer

    agent_reflection_bp,



    # Adaptation Layer

    agent_adaptation_bp,



    # Evolution Layer

    agent_evolution_bp

]




# =====================================================
# Register Blueprints
# =====================================================

for blueprint in BLUEPRINTS:

    try:

        app.register_blueprint(
            blueprint
        )

    except Exception as error:

        print(
            f"Blueprint registration failed: {error}"
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

            "Autonomous AI Decision Intelligence Platform",



        "layers":[


            "Core Intelligence",

            "Career Intelligence",

            "Simulation Intelligence",

            "Memory Intelligence",

            "Memory Consolidation Intelligence",

            "Knowledge Graph Intelligence",

            "Reasoning Intelligence",

            "Decision Orchestration",

            "Autonomous Agent Intelligence",

            "Agent Evolution Intelligence"


        ],



        "agent_system":{


            "status":

                "operational",


            "agents":

                8,


            "autonomous_cycle":[


                "Observe",

                "Retrieve Memory",

                "Consolidate Memory",

                "Reason",

                "Plan",

                "Communicate",

                "Govern",

                "Execute",

                "Learn",

                "Reflect",

                "Adapt",

                "Evolve",

                "Optimize"


            ]

        },



        "engines":[


            "AI Agent Runtime Engine v1",

            "AI Agent Tool Execution Engine v1",

            "AI Agent Planner Engine v1",

            "AI Agent Supervisor Engine v1",

            "AI Agent Memory Engine v1",

            "AI Agent Learning Engine v1",

            "AI Autonomous Decision Loop Engine v1",

            "AI Multi Agent Coordination Engine v1",

            "AI Agent Communication Engine v1",

            "AI Agent Governance Engine v1",

            "AI Agent Reflection Engine v1",

            "AI Agent Adaptation Engine v1",

            "AI Memory Consolidation Engine v1",

            "AI Agent Evolution Engine v1"


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


        "autonomous_agents":{


            "enabled":

                True,


            "total_agents":

                8,


            "self_improvement":

                "enabled"

        },


        "modules":[


            "Decision Intelligence",

            "Career Intelligence",

            "Digital Twin Intelligence",

            "Decision Memory Intelligence",

            "Memory Consolidation Intelligence",

            "Knowledge Graph Intelligence",

            "Decision Reasoning Intelligence",

            "Decision Orchestration Intelligence",

            "Agent Runtime Intelligence",

            "Agent Planning Intelligence",

            "Agent Supervisor Intelligence",

            "Agent Memory Intelligence",

            "Agent Learning Intelligence",

            "Agent Loop Intelligence",

            "Multi Agent Intelligence",

            "Agent Communication Intelligence",

            "Agent Governance Intelligence",

            "Agent Reflection Intelligence",

            "Agent Adaptation Intelligence",

            "Agent Evolution Intelligence"


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