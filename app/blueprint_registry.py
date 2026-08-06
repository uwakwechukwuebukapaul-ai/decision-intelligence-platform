"""
Sentinel DNA - Blueprint Registry

Centralized Flask blueprint registration layer.

Responsible for:

- Registering application blueprints
- Preventing duplicate registration
- Keeping application factory clean
- Supporting optional modules
- Supporting future plugin discovery
- Supporting intelligence service expansion
"""

from __future__ import annotations

import logging

from importlib import import_module

from flask import Flask
from flask.blueprints import Blueprint


logger = logging.getLogger(__name__)



def register_blueprint(
    app: Flask,
    blueprint: Blueprint,
    *,
    url_prefix: str | None = None,
) -> None:
    """
    Safely register a Flask blueprint.
    """


    if blueprint.name in app.blueprints:

        logger.warning(
            "Blueprint already registered: %s",
            blueprint.name,
        )

        return



    if url_prefix:

        app.register_blueprint(
            blueprint,
            url_prefix=url_prefix,
        )

    else:

        app.register_blueprint(
            blueprint
        )


    logger.info(
        "Registered blueprint: %s",
        blueprint.name,
    )



def register_blueprints(
    app: Flask,
) -> None:
    """
    Register all Sentinel DNA application blueprints.

    Includes:

    - Control Plane
    - Intelligence Fabric
    - IOC Intelligence
    - Knowledge Graph
    - Investigation Platform
    - Analyst Workspace
    - Copilot
    - Autonomous Operations
    - AI SOC Agent Gateway
    """



    modules = [


        # =====================================
        # Control Plane
        # =====================================

        (
            "app.routes.intelligence_control_plane",
            "intelligence_control_plane_bp",
        ),


        (
            "app.routes.intelligence_execution",
            "intelligence_execution_bp",
        ),



        # =====================================
        # Intelligence APIs
        # =====================================

        (
            "app.routes.api.v1.intelligence",
            "intelligence_api_bp",
        ),


        (
            "app.routes.api.v1.ioc",
            "ioc_api_bp",
        ),


        (
            "app.routes.api.v1.graph",
            "graph_api_bp",
        ),


        (
            "app.routes.api.v1.graph_intelligence",
            "graph_intelligence_api_bp",
        ),



        # =====================================
        # Investigation Platform
        # =====================================

        (
            "app.routes.api.v1.investigation",
            "investigation_api_bp",
        ),



        # =====================================
        # Sentinel DNA AI SOC Gateway
        # =====================================

        (
            "app.api.agent_api",
            "agent_bp",
        ),



        # =====================================
        # Analyst Workspace
        # =====================================

        (
            "app.routes.api.v1.workspace",
            "workspace_api_bp",
        ),



        # =====================================
        # Reporting
        # =====================================

        (
            "app.routes.api.v1.report",
            "report_api_bp",
        ),



        # =====================================
        # AI Copilot
        # =====================================

        (
            "app.routes.api.v1.copilot",
            "copilot_api_bp",
        ),



        # =====================================
        # Autonomous Intelligence
        # =====================================

        (
            "app.routes.api.v1.autonomous",
            "autonomous_api_bp",
        ),


        (
            "app.routes.api.v1.orchestration",
            "orchestration_api_bp",
        ),


        (
            "app.routes.api.v1.correlation",
            "correlation_api_bp",
        ),


        (
            "app.routes.api.v1.campaign",
            "campaign_api_bp",
        ),


        (
            "app.routes.api.v1.threat_actor",
            "threat_actor_api_bp",
        ),

    ]



    loaded_blueprints = []



    for module_name, attribute_name in modules:


        try:

            module = import_module(
                module_name
            )


            blueprint = getattr(
                module,
                attribute_name,
            )


            register_blueprint(
                app,
                blueprint,
            )


            loaded_blueprints.append(
                blueprint.name
            )



        except ModuleNotFoundError:

            logger.warning(
                "Optional blueprint not found: %s",
                module_name,
            )



        except AttributeError:

            logger.error(
                "Blueprint attribute missing: %s.%s",
                module_name,
                attribute_name,
            )



        except Exception as exc:

            logger.exception(
                "Failed loading blueprint %s: %s",
                module_name,
                exc,
            )



    logger.info(
        "Blueprint registration completed. Loaded: %s",
        loaded_blueprints,
    )



# Backward compatibility

register_all_blueprints = register_blueprints