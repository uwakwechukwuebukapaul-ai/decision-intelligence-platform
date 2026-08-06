"""
Sentinel DNA - Blueprint Registry

Centralized Flask blueprint registration layer.

Responsible for:
- Registering application blueprints
- Preventing duplicate registration
- Keeping factory clean
- Supporting future plugin discovery
"""

from __future__ import annotations

import logging

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
            "app.routes.api.v1.investigation",
            "investigation_api_bp",
        ),

    ]



    for module_name, attribute_name in modules:

        try:

            module = __import__(
                module_name,
                fromlist=[attribute_name],
            )


            blueprint = getattr(
                module,
                attribute_name,
            )


            register_blueprint(
                app,
                blueprint,
            )


        except Exception as exc:

            logger.exception(
                "Failed loading blueprint %s: %s",
                module_name,
                exc,
            )



# Backward compatibility

register_all_blueprints = register_blueprints