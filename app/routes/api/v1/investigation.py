"""
Sentinel DNA

Investigation API

Provides:

- IOC investigation
- Investigation timeline
- Investigation memory
- Investigation reports
- AI SOC investigation workflow
"""

from __future__ import annotations

import uuid

from flask import (
    Blueprint,
    jsonify,
    request,
)

from app.intelligence.ioc.fusion import IntelligenceFusion
from app.intelligence.ioc.timeline import (
    TimelineEngine,
    InvestigationMemory,
)
from app.intelligence.ioc.workflow import IOCCaseOrchestrator

from app.investigations import Investigation

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

# ==========================================================
# Blueprint
# ==========================================================

investigation_api_bp = Blueprint(
    "investigation_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)

# ==========================================================
# IOC Services
# ==========================================================

fusion = IntelligenceFusion()

timeline_engine = TimelineEngine()

memory_engine = InvestigationMemory()

workflow = IOCCaseOrchestrator()

# ==========================================================
# AI Agent Registry
# ==========================================================

agent_registry = AgentRegistry()

agent_registry.register(EvidenceAgent())

agent_registry.register(ThreatIntelligenceAgent())

agent_registry.register(MitreAgent())

agent_registry.register(RiskAgent())

agent_registry.register(ResponseAgent())

investigation_orchestrator = InvestigationOrchestrator(
    agent_registry
)

# ==========================================================
# IOC Timeline
# ==========================================================


@investigation_api_bp.get("/ioc/<string:indicator>/timeline")
def get_ioc_timeline(indicator: str):

    intelligence = fusion.analyze(indicator)

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


# ==========================================================
# IOC Memory
# ==========================================================


@investigation_api_bp.get("/ioc/<string:indicator>/memory")
def get_ioc_memory(indicator: str):

    memory = memory_engine.get_memory(indicator)

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


# ==========================================================
# IOC Report
# ==========================================================


@investigation_api_bp.get("/ioc/<string:indicator>/report")
def get_ioc_report(indicator: str):

    intelligence = fusion.analyze(indicator)

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


# ==========================================================
# AI Investigation
# ==========================================================


@investigation_api_bp.post("/investigation")
def create_ai_investigation():

    data = request.get_json(force=True)

    investigation = Investigation(
        investigation_id="INV-" + str(uuid.uuid4())[:8],
        case_id=data["case_id"],
        evidence=data.get("evidence", []),
    )

    result = investigation_orchestrator.investigate(
        investigation
    )

    return jsonify(result)