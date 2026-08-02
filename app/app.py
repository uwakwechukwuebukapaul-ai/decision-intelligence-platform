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
# Intelligence Layer Routes
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
# Knowledge Intelligence
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
# Autonomous Agent Intelligence
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
# Agent Communication
# =====================================================

from app.routes.agent_communication import agent_communication_bp



# =====================================================
# Agent Governance
# =====================================================

from app.routes.agent_governance import agent_governance_bp



# =====================================================
# Self Improvement Intelligence
# =====================================================

from app.routes.agent_reflection import agent_reflection_bp
from app.routes.agent_adaptation import agent_adaptation_bp
from app.routes.agent_evolution import agent_evolution_bp
from app.routes.agent_optimization import agent_optimization_bp
from app.routes.agent_meta_learning import agent_meta_learning_bp



# =====================================================
# Collective Intelligence
# =====================================================

from app.routes.collective_intelligence import (
    collective_intelligence_bp
)



# =====================================================
# Swarm Intelligence
# =====================================================

from app.routes.agent_swarm import (
    agent_swarm_bp
)

# =====================================================
# Autonomous Mission Intelligence
# =====================================================

from app.routes.autonomous_mission import (
    autonomous_mission_bp
)



# =====================================================
# Autonomous Goal Intelligence
# =====================================================

from app.routes.autonomous_goal import (
    autonomous_goal_bp
)



# =====================================================
# Strategic Planning Intelligence
# =====================================================

from app.routes.strategic_planning import (
    strategic_planning_bp
)



# =====================================================
# Execution Management Intelligence
# =====================================================

from app.routes.execution_management import (
    execution_management_bp
)



# =====================================================
# Performance Optimization Intelligence
# =====================================================

from app.routes.performance_optimization import (
    performance_optimization_bp
)



# =====================================================
# Autonomous Orchestration Intelligence
# =====================================================

from app.routes.autonomous_orchestrator import (
    autonomous_orchestrator_bp
)



# =====================================================
# Cognitive Core Intelligence
# =====================================================

from app.routes.cognitive_core import (
    cognitive_core_bp
)



# =====================================================
# Autonomous Intelligence Fabric
# =====================================================

from app.routes.autonomous_fabric import (
    autonomous_fabric_bp
)



# =====================================================
# Autonomous Operating System
# =====================================================

from app.routes.autonomous_operating_system import (
    autonomous_operating_system_bp
)



# =====================================================
# Collective Operating Intelligence
# =====================================================

from app.routes.collective_operating_intelligence import (
    collective_operating_intelligence_bp
)



# =====================================================
# Application Metadata
# =====================================================

APP_NAME = "Decision Intelligence Platform"

APP_VERSION = "5.0"

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


    # =================================================
    # Core Platform
    # =================================================

    profile_bp,
    analysis_bp,
    auth_bp,
    reports_bp,
    dashboard_bp,
    progress_bp,
    certification_bp,
    learning_bp,
    learning_progress_bp,



    # =================================================
    # Intelligence Layer
    # =================================================

    skill_analysis_bp,
    career_report_bp,
    decision_bp,
    recommendation_bp,
    advisor_bp,
    mentor_bp,
    coach_bp,
    intelligence_bp,



    # =================================================
    # Simulation Layer
    # =================================================

    digital_twin_bp,
    career_simulation_bp,
    career_evolution_bp,



    # =================================================
    # Memory Layer
    # =================================================

    memory_bp,
    memory_consolidation_bp,



    # =================================================
    # Knowledge Layer
    # =================================================

    intelligence_graph_bp,



    # =================================================
    # Reasoning Layer
    # =================================================

    decision_reasoning_bp,



    # =================================================
    # Decision Orchestration
    # =================================================

    decision_orchestrator_bp,



    # =================================================
    # Autonomous Agents
    # =================================================

    agent_runtime_bp,
    agent_tools_bp,
    agent_planner_bp,
    agent_supervisor_bp,
    agent_memory_bp,
    agent_learning_bp,
    agent_loop_bp,



    # =================================================
    # Multi Agent
    # =================================================

    multi_agent_bp,



    # =================================================
    # Agent Communication
    # =================================================

    agent_communication_bp,



    # =================================================
    # Agent Governance
    # =================================================

    agent_governance_bp,



    # =================================================
    # Self Improvement
    # =================================================

    agent_reflection_bp,
    agent_adaptation_bp,
    agent_evolution_bp,
    agent_optimization_bp,
    agent_meta_learning_bp,



    # =================================================
    # Collective Intelligence
    # =================================================

    collective_intelligence_bp,



    # =================================================
    # Swarm Intelligence
    # =================================================

    agent_swarm_bp,



    # =================================================
    # Autonomous Intelligence Stack
    # =================================================

    autonomous_mission_bp,

    autonomous_goal_bp,

    strategic_planning_bp,

    execution_management_bp,

    performance_optimization_bp,

    autonomous_orchestrator_bp,

    cognitive_core_bp,

    autonomous_fabric_bp,

    autonomous_operating_system_bp,

    collective_operating_intelligence_bp


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

@app.route("/", methods=["GET"])
def home():

    return {

        "platform":

            APP_NAME,


        "version":

            APP_VERSION,


        "status":

            APP_STATUS,


        "message":

            "Autonomous Decision Intelligence Platform is operational"

    }




# =====================================================
# Health Monitoring Endpoint
# =====================================================

@app.route("/health", methods=["GET"])
def health():

    return {


        "status":

            "healthy",


        "platform":

            APP_NAME,


        "version":

            APP_VERSION,


        "services":

            {

                "database":

                    "connected",


                "intelligence_engine":

                    "active",


                "autonomous_agents":

                    "running",


                "collective_intelligence":

                    "enabled",


                "operating_system_layer":

                    "active"

            }

    }




# =====================================================
# Platform Information Endpoint
# =====================================================

@app.route("/api/info", methods=["GET"])
def platform_info():

    return {


        "platform":

            APP_NAME,


        "version":

            APP_VERSION,


        "architecture":

            [

                "Cognitive Core",

                "Autonomous Fabric",

                "Autonomous Operating System",

                "Collective Operating Intelligence",

                "Decision Intelligence"

            ],


        "capabilities":

            [

                "Autonomous Planning",

                "Mission Intelligence",

                "Goal Generation",

                "Execution Management",

                "Performance Optimization",

                "Agent Orchestration",

                "Continuous Learning"

            ],


        "status":

            "operational"

    }




# =====================================================
# Application Runner
# =====================================================

if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )