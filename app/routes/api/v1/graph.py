"""
Sentinel DNA

IOC Graph API Routes
"""

from flask import (
    Blueprint,
    jsonify,
)


from app.intelligence.ioc.api import (
    IOCGraphAPI,
)



graph_api_bp = Blueprint(
    "graph_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)


graph_service = IOCGraphAPI()



@graph_api_bp.route(
    "/ioc/<indicator>/graph",
    methods=["GET"],
)
def ioc_graph(indicator):


    result = graph_service.build_graph(
        indicator,
        "unknown",
    )


    return jsonify(
        {
            "service": "ioc-graph-intelligence",
            "result": result,
        }
    )