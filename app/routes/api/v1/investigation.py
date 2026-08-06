"""
Sentinel DNA

Investigation API

Provides:

- IOC investigation
- AI agent investigation workflow
- Investigation timeline
- Investigation memory
- Complete investigation report
"""

from __future__ import annotations


import uuid


from flask import (
    Blueprint,
    jsonify,
    request,
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


from app.investigations import (
    Investigation,
)


from app.ai.agents import (
    AgentRegistry,
    EvidenceAgent,
    ThreatIntelligenceAgent,
    MitreAgent,
    RiskAgent,
    ResponseAgent,
)


from app.ai.investigation_orchestrator import (
    InvestigationOrchestrator,
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



# =====================================
# AI Investigation Runtime
# =====================================


registry = AgentRegistry()


registry.register(
    EvidenceAgent()
)

registry.register(
    ThreatIntelligenceAgent()
)

registry.register(
    MitreAgent()
)

registry.register(
    RiskAgent()
)

registry.register(
    ResponseAgent()
)



orchestrator = InvestigationOrchestrator(
    registry
)



# =====================================
# IOC Timeline
# =====================================


@investigation_api_bp.route(
    "/ioc/<indicator>/timeline",
    methods=["GET"],
)
def get_ioc_timeline(indicator):


    intelligence = fusion.analyze(
        indicator
    )


    timeline = timeline_engine.build_from_intelligence(
        intelligence
    )


    return jsonify(
        {
            "service":
            "ioc-investigation-timeline",

            "indicator":
            indicator,

            "timeline":
            timeline,
        }
    )



# =====================================
# IOC Memory
# =====================================


@investigation_api_bp.route(
    "/ioc/<indicator>/memory",
    methods=["GET"],
)
def get_ioc_memory(indicator):


    memory = memory_engine.get_memory(
        indicator
    )


    if memory is None:

        memory = memory_engine.create_memory(
            indicator
        )


    return jsonify(
        {
            "service":
            "ioc-investigation-memory",

            "indicator":
            indicator,

            "memory":
            memory,
        }
    )



# =====================================
# IOC Report
# =====================================


@investigation_api_bp.route(
    "/ioc/<indicator>/report",
    methods=["GET"],
)
def get_ioc_report(indicator):


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
            "service":
            "ioc-investigation-report",

            "indicator":
            indicator,

            "investigation":
            investigation,

            "timeline":
            timeline,

        }
    )



# =====================================
# AI SOC Investigation
# =====================================


@investigation_api_bp.route(
    "/investigation",
    methods=["POST"],
)
def create_ai_investigation():


    data = request.get_json()


    investigation_id = (
        "INV-"
        +
        str(uuid.uuid4())[:8]
    )


    investigation = Investigation(

        investigation_id,

        data.get(
            "case_id"
        ),

        data.get(
            "evidence",
            []
        )

    )


    result = orchestrator.investigate(
        investigation
    )


    return jsonify(
        result
    )