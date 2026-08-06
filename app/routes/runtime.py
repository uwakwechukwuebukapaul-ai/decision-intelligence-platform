"""
Runtime Management API
"""

from flask import Blueprint, jsonify

from app.core.lifecycle import lifecycle


runtime_bp = Blueprint(
    "runtime",
    __name__,
    url_prefix="/runtime",
)


@runtime_bp.route("/health", methods=["GET"])
def health():

    return jsonify(
        lifecycle.health()
    )


@runtime_bp.route("/start", methods=["POST"])
def start():

    lifecycle.start()

    return jsonify(
        {
            "status": "started",
            "runtime": lifecycle.health()
        }
    )


@runtime_bp.route("/shutdown", methods=["POST"])
def shutdown():

    lifecycle.shutdown()

    return jsonify(
        {
            "status": "shutdown",
            "runtime": lifecycle.health()
        }
    )