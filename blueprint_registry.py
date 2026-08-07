"""
Sentinel DNA - Blueprint Registry

Centralized Flask blueprint registration layer.

Responsible for:

- Registering application blueprints
- Preventing duplicate registration
- Supporting optional modules
- Supporting future plugin discovery
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
    Register Sentinel DNA application blueprints.
    """

    modules = [

        (
            "app.routes.api.v1.investigation",
            "investigation_api_bp",
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
            "app.routes.api.v1.report",
            "report_api_bp",
        ),

        (
            "app.routes.api.v1.copilot",
            "copilot_api_bp",
        ),

    ]


    loaded = []


    for module_name, blueprint_name in modules:

        try:

            module = import_module(
                module_name
            )


            blueprint = getattr(
                module,
                blueprint_name,
            )


            register_blueprint(
                app,
                blueprint,
            )


            loaded.append(
                blueprint.name
            )


        except ModuleNotFoundError:

            logger.warning(
                "Optional blueprint missing: %s",
                module_name,
            )


        except AttributeError:

            logger.error(
                "Blueprint missing: %s",
                blueprint_name,
            )


        except Exception as exc:

            logger.exception(
                "Blueprint load failed: %s",
                exc,
            )


    logger.info(
        "Blueprint registration completed: %s",
        loaded,
    )



# Backward compatibility

register_all_blueprints = register_blueprints