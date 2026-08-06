from flask import Blueprint, jsonify, request


intelligence_bp = Blueprint(
    "intelligence",
    __name__,
    url_prefix="/intelligence"
)


SUPPORTED_CAPABILITIES = [
    "reasoning",
    "analysis",
    "planning"
]


@intelligence_bp.route(
    "/execute",
    methods=["POST"]
)
def execute():

    data = request.get_json() or {}

    capability = data.get(
        "capability"
    )


    if capability not in SUPPORTED_CAPABILITIES:

        return jsonify(
            {
                "status": "error",
                "message":
                    "Unsupported capability"
            }
        ), 404



    return jsonify(
        {
            "status":
                "success",

            "capability":
                capability,

            "objective":
                data.get(
                    "objective"
                ),

            "user_id":
                data.get(
                    "user_id"
                )
        }
    ), 200