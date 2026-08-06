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
    Register all application blueprints.

    Central registry for:

    - Intelligence services
    - API gateways
    - Analyst workspace
    - Copilot services
    - Reporting services
    - Autonomous investigation
    - Investigation orchestration
    - Knowledge graph intelligence
    - Future plugins
    """


    modules = [

        (
            "app.routes.intelligence_control_plane",
            "intelligence_control_plane_bp",
        ),


        (
            "app.routes.intelligence_execution",
            "intelligence_execution_bp",
        ),


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


        (
            "app.routes.api.v1.investigation",
            "investigation_api_bp",
        ),


        (
            "app.routes.api.v1.workspace",
            "workspace_api_bp",
        ),


        (
            "app.routes.api.v1.report",
            "report_api_bp",
        ),


        (
            "app.routes.api.v1.copilot",
            "copilot_api_bp",
        ),


        (
            "app.routes.api.v1.autonomous",
            "autonomous_api_bp",
        ),


        (
            "app.routes.api.v1.orchestration",
            "orchestration_api_bp",
        ),

    ]





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
        list(app.blueprints.keys()),
    )







# Backward compatibility

register_all_blueprints = register_blueprints