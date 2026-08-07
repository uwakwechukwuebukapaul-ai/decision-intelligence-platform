"""
Sentinel DNA Agent Executor

Executes AI agents within the Intelligence Runtime.
"""

from __future__ import annotations


class AgentExecutor:
    """
    Executes registered AI agents.
    """

    def __init__(self, registry):
        self.registry = registry

    def execute(self, job):
        """
        Execute an IntelligenceJob.
        """

        # Find an agent that supports the requested capability
        agent = self.registry.get(job.capability)

        if agent is None:
            job.status = "failed"

            return {
                "status": "failed",
                "agent": None,
                "reason": f"No agent registered for '{job.capability}'",
            }

        try:
            output = agent.execute(job.payload)

            job.status = "completed"

            return {
                "status": "completed",
                "agent": agent.name,
                "result": output,
            }

        except Exception as exc:

            job.status = "failed"

            return {
                "status": "failed",
                "agent": agent.name,
                "reason": str(exc),
            }