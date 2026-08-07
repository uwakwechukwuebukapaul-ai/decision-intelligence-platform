"""
Sentinel DNA Application Factory

Responsible for:

- Creating Flask instance
- Loading configuration
- Registering blueprints
- Preparing application extensions
"""

from __future__ import annotations

from flask import Flask


def create_app() -> Flask:
    """
    Application factory.
    """

    app = Flask(
        __name__
    )


    # Register all application blueprints

    from app.blueprint_registry import (
        register_blueprints,
    )


    register_blueprints(
        app
    )


    return app