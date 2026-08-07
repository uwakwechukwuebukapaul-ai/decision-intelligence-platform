"""
Sentinel DNA Investigation Orchestrator

Controls complete AI SOC investigations.

Responsibilities:

- Starts investigation lifecycle
- Selects AI agents
- Executes investigation pipeline
- Collects agent intelligence
- Completes investigation
- Generates investigation response
"""

from __future__ import annotations

from .execution_pipeline import ExecutionPipeline


class InvestigationOrchestrator:
    """
    Coordinates multi-agent SOC investigations.
    """

    def __init__(self, agent_registry):
        self.pipeline = ExecutionPipeline(agent_registry)

    def investigate(self, investigation):
        """
        Execute complete investigation workflow.
        """

        # Start investigation
        investigation.start()

        # Ordered AI investigation chain
        agents = [
            "EvidenceAgent",
            "ThreatIntelligenceAgent",
            "MitreAgent",
            "RiskAgent",
            "ResponseAgent",
        ]

        # Execute agents
        results = self.pipeline.execute(
            investigation,
            agents,
        )

        # Complete investigation
        investigation.complete()

        return {
            "investigation_id": investigation.investigation_id,
            "status": investigation.state.status.value,
            "agents_executed": agents,
            "results": results,
            "report": investigation.report(),
        }