"""
Sentinel DNA - Blueprint Registry

Centralized Flask blueprint registration layer.

Responsible for:
- Registering application blueprints
- Preventing duplicate registration per Flask app
- Keeping the application factory clean
- Preparing for future plugin/module discovery
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask import Flask
    from flask.blueprints import Blueprint

logger = logging.getLogger(__name__)


def register_blueprint(
    app: "Flask",
    blueprint: "Blueprint",
    *,
    url_prefix: str | None = None,
) -> None:
    """
    Register a Flask blueprint safely.

    Duplicate detection is performed against the current
    Flask application instance instead of using global state.
    """

    if blueprint.name in app.blueprints:
        logger.warning(
            "Blueprint already registered: %s",
            blueprint.name,
        )
        return

    if url_prefix is not None:
        app.register_blueprint(
            blueprint,
            url_prefix=url_prefix,
        )
    else:
        app.register_blueprint(
            blueprint,
        )

    logger.info(
        "Registered blueprint: %s",
        blueprint.name,
    )


def register_blueprints(app: "Flask") -> None:
    """
    Register all application blueprints.

    Called once from create_app().
    """

    blueprints: list[tuple["Blueprint", str | None]] = []

    # ---------------------------------------------
    # Intelligence Control Plane
    # ---------------------------------------------
    try:
        from app.routes.intelligence_control_plane import (
            intelligence_control_plane_bp,
        )

        blueprints.append(
            (
                intelligence_control_plane_bp,
                None,
            )
        )

    except Exception as exc:
        logger.exception(
            "Failed loading intelligence control plane: %s",
            exc,
        )

    # ---------------------------------------------
    # Intelligence Execution
    # ---------------------------------------------
    try:
        from app.routes.intelligence_execution import (
            intelligence_execution_bp,
        )

        blueprints.append(
            (
                intelligence_execution_bp,
                None,
            )
        )

    except Exception as exc:
        logger.exception(
            "Failed loading intelligence execution routes: %s",
            exc,
        )

    # ---------------------------------------------
    # Register Loaded Blueprints
    # ---------------------------------------------
    for blueprint, prefix in blueprints:
        register_blueprint(
            app,
            blueprint,
            url_prefix=prefix,
        )


# Backward compatibility
register_all_blueprints = register_blueprints