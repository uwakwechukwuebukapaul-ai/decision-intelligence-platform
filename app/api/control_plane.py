from flask import Blueprint, jsonify


control_plane_bp = Blueprint(
    "control_plane",
    __name__,
    url_prefix="/control-plane"
)


@control_plane_bp.route(
    "/status",
    methods=["GET"]
)
def status():

    return jsonify(
        {
            "status": "online",
            "service": "control-plane"
        }
    ), 200



@control_plane_bp.route(
    "/health",
    methods=["GET"]
)
def health():

    return jsonify(
        {
            "status": "healthy",
            "service": "control-plane"
        }
    ), 200