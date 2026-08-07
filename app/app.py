"""
Sentinel DNA

Application Entry Point

Responsible for:

- Creating Flask application instance
- Exposing WSGI application
- Running development server
"""

from __future__ import annotations

from app.factory import create_app


# Flask application instance
app = create_app()


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )