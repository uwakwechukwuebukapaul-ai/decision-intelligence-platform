"""
Agent Health Monitor
"""


from datetime import UTC, datetime


class AgentHealthMonitor:

    def check(self, agent):

        return {

            "agent":
                agent.metadata.name,

            "status":
                agent.metadata.status,

            "healthy":
                agent.metadata.status == "active",

            "checked_at":
                datetime.now(
                    UTC
                ).isoformat(),

        }