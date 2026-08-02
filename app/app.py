from flask import Flask
import os


# =====================================================
# Database
# =====================================================

from app.database.db import engine, Base



# =====================================================
# Models Registration
# =====================================================

from app.models import (
    UserProfile,
    AIReport,
    SkillProgress,
    LearningProgress
)



# =====================================================
# Core Platform Routes
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
# Simulation Intelligence
# =====================================================

from app.routes.digital_twin import digital_twin_bp
from app.routes.career_simulation import career_simulation_bp
from app.routes.career_evolution import career_evolution_bp



# =====================================================
# Memory Intelligence
# =====================================================

from app.routes.memory import memory_bp
from app.routes.memory_consolidation import memory_consolidation_bp



# =====================================================
# Knowledge Graph
# =====================================================

from app.routes.intelligence_graph import intelligence_graph_bp



# =====================================================
# Reasoning Intelligence
# =====================================================

from app.routes.decision_reasoning import decision_reasoning_bp



# =====================================================
# Decision Orchestration
# =====================================================

from app.routes.decision_orchestrator import decision_orchestrator_bp



# =====================================================
# Autonomous Agent Foundation
# =====================================================

from app.routes.agent_runtime import agent_runtime_bp
from app.routes.agent_tools import agent_tools_bp
from app.routes.agent_planner import agent_planner_bp
from app.routes.agent_supervisor import agent_supervisor_bp
from app.routes.agent_memory import agent_memory_bp
from app.routes.agent_learning import agent_learning_bp
from app.routes.agent_loop import agent_loop_bp



# =====================================================
# Multi Agent Intelligence
# =====================================================

from app.routes.multi_agent import multi_agent_bp



# =====================================================
# Communication + Governance
# =====================================================

from app.routes.agent_communication import agent_communication_bp
from app.routes.agent_governance import agent_governance_bp



# =====================================================
# Self Improvement Layer
# =====================================================

from app.routes.agent_reflection import agent_reflection_bp
from app.routes.agent_adaptation import agent_adaptation_bp
from app.routes.agent_evolution import agent_evolution_bp
from app.routes.agent_optimization import agent_optimization_bp
from app.routes.agent_meta_learning import agent_meta_learning_bp



# =====================================================
# Collective Intelligence
# =====================================================

from app.routes.collective_intelligence import collective_intelligence_bp



# =====================================================
# Agent Swarm
# =====================================================

from app.routes.agent_swarm import agent_swarm_bp



# =====================================================
# Autonomous Mission
# =====================================================

from app.routes.autonomous_mission import autonomous_mission_bp



# =====================================================
# Autonomous Goal
# =====================================================

from app.routes.autonomous_goal import autonomous_goal_bp



# =====================================================
# Strategic Planning
# =====================================================

from app.routes.strategic_planning import strategic_planning_bp



# =====================================================
# Execution Management
# =====================================================

from app.routes.execution_management import execution_management_bp



# =====================================================
# Performance Optimization
# =====================================================

from app.routes.performance_optimization import performance_optimization_bp



# =====================================================
# Autonomous Orchestrator
# =====================================================

from app.routes.autonomous_orchestrator import autonomous_orchestrator_bp



# =====================================================
# Cognitive Core Intelligence
# =====================================================

from app.routes.cognitive_core import cognitive_core_bp



APP_NAME = "Decision Intelligence Platform"

APP_VERSION = "5.0"

APP_STATUS = "running"



app = Flask(

    __name__,

    template_folder=os.path.join(

        os.path.dirname(

            os.path.dirname(__file__)

        ),

        "templates"

    )

)



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



    # AI Intelligence

    skill_analysis_bp,
    career_report_bp,
    decision_bp,
    recommendation_bp,
    advisor_bp,
    mentor_bp,
    coach_bp,
    intelligence_bp,



    # Simulation Intelligence

    digital_twin_bp,
    career_simulation_bp,
    career_evolution_bp,



    # Memory Intelligence

    memory_bp,
    memory_consolidation_bp,



    # Knowledge Graph

    intelligence_graph_bp,



    # Reasoning Intelligence

    decision_reasoning_bp,



    # Decision Orchestration

    decision_orchestrator_bp,



    # Autonomous Agent System

    agent_runtime_bp,
    agent_tools_bp,
    agent_planner_bp,
    agent_supervisor_bp,
    agent_memory_bp,
    agent_learning_bp,
    agent_loop_bp,



    # Multi Agent Intelligence

    multi_agent_bp,



    # Communication Layer

    agent_communication_bp,



    # Governance Layer

    agent_governance_bp,



    # Self Improvement

    agent_reflection_bp,
    agent_adaptation_bp,
    agent_evolution_bp,
    agent_optimization_bp,
    agent_meta_learning_bp,



    # Collective Intelligence

    collective_intelligence_bp,



    # Agent Swarm Intelligence

    agent_swarm_bp,



    # Autonomous Mission Intelligence

    autonomous_mission_bp,



    # Autonomous Goal Intelligence

    autonomous_goal_bp,



    # Strategic Planning Intelligence

    strategic_planning_bp,



    # Execution Management Intelligence

    execution_management_bp,



    # Performance Optimization Intelligence

    performance_optimization_bp,



    # Autonomous Orchestration Intelligence

    autonomous_orchestrator_bp,



    # Cognitive Core Intelligence

    cognitive_core_bp

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

            "AI Decision Intelligence Platform",


        "intelligence_state":

            "Autonomous Cognitive Swarm Intelligence Network",



        "layers":[


            "Core Intelligence",

            "Career Intelligence",

            "Digital Twin Intelligence",

            "Memory Intelligence",

            "Knowledge Graph Intelligence",

            "Reasoning Intelligence",

            "Decision Orchestration",

            "Autonomous Agents",

            "Self Improvement",

            "Collective Intelligence",

            "Swarm Intelligence",

            "Autonomous Mission Intelligence",

            "Strategic Planning Intelligence",

            "Execution Intelligence",

            "Performance Optimization",

            "Autonomous Orchestration",

            "Cognitive Core Intelligence"


        ],



        "agent_system":{


            "status":

                "operational",


            "architecture":

                "Autonomous Cognitive Multi Agent Network",


            "agents":

                6,


            "autonomous_cycle":[


                "Observe",

                "Retrieve Memory",

                "Reason",

                "Plan",

                "Collaborate",

                "Execute",

                "Monitor",

                "Learn",

                "Reflect",

                "Adapt",

                "Optimize",

                "Evolve"

            ]

        },



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


        "architecture":

            "Autonomous Cognitive Intelligence Platform",


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

            "Digital Twin",

            "Memory Intelligence",

            "Knowledge Graph",

            "Decision Reasoning",

            "Decision Orchestration",


            "Agent Runtime",

            "Agent Planning",

            "Agent Memory",

            "Agent Learning",

            "Agent Loop",


            "Multi Agent Collaboration",

            "Agent Communication",

            "Agent Governance",


            "Agent Reflection",

            "Agent Adaptation",

            "Agent Evolution",

            "Agent Optimization",

            "Agent Meta Learning",


            "Collective Intelligence",

            "Consensus Intelligence",

            "Knowledge Pool",


            "Agent Swarm Intelligence",


            "Autonomous Mission Engine",

            "Autonomous Goal Engine",

            "Strategic Planning Engine",

            "Execution Management Engine",

            "Performance Optimization Engine",

            "Autonomous Orchestrator Engine",

            "Cognitive Core Engine"


        ],



        "autonomous_agents":{


            "status":

                "online",


            "total_agents":

                6,


            "architecture":

                "Collaborative Cognitive Autonomous Swarm"

        }

    }





# =====================================================
# Application Runner
# =====================================================


if __name__ == "__main__":


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )  