"""
Sentinel DNA

IOC Investigation API

Provides:
- Investigation timeline
- Investigation memory
- Complete investigation report
"""

from flask import (
    Blueprint,
    jsonify,
)

from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)

from app.intelligence.ioc.timeline import (
    TimelineEngine,
    InvestigationMemory,
)

from app.intelligence.ioc.workflow import (
    IOCCaseOrchestrator,
)



investigation_api_bp = Blueprint(
    "investigation_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)


fusion = IntelligenceFusion()

timeline_engine = TimelineEngine()

memory_engine = InvestigationMemory()

workflow = IOCCaseOrchestrator()



@investigation_api_bp.route(
    "/ioc/<indicator>/timeline",
    methods=["GET"],
)
def get_ioc_timeline(
    indicator: str,
):

    intelligence = fusion.analyze(
        indicator
    )


    timeline = timeline_engine.build_from_intelligence(
        intelligence
    )


    return jsonify(
        {
            "service": "ioc-investigation-timeline",
            "indicator": indicator,
            "timeline": timeline,
        }
    )



@investigation_api_bp.route(
    "/ioc/<indicator>/memory",
    methods=["GET"],
)
def get_ioc_memory(
    indicator: str,
):

    memory = memory_engine.get_memory(
        indicator
    )


    if memory is None:

        memory = memory_engine.create_memory(
            indicator
        )


    return jsonify(
        {
            "service": "ioc-investigation-memory",
            "indicator": indicator,
            "memory": memory,
        }
    )



@investigation_api_bp.route(
    "/ioc/<indicator>/report",
    methods=["GET"],
)
def get_ioc_report(
    indicator: str,
):

    intelligence = fusion.analyze(
        indicator
    )


    investigation = workflow.process(
        intelligence
    )


    timeline = timeline_engine.build_from_intelligence(
        intelligence
    )


    return jsonify(
        {
            "service": "ioc-investigation-report",

            "indicator": indicator,

            "investigation": investigation,

            "timeline": timeline,

        }
    )