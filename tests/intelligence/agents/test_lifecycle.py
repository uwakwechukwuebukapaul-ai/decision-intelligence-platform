"""
Tests for Agent Lifecycle
"""


from app.intelligence.agents import BaseAgent
from app.intelligence.agents.lifecycle import AgentLifecycle
from app.intelligence.agents.health_monitor import (
    AgentHealthMonitor,
)
from app.intelligence.agents.metrics import (
    AgentMetrics,
)


class DemoAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Demo Agent",
            version="1.0.0",
            capabilities=[
                "demo"
            ],
        )

    def execute(
        self,
        payload,
    ):

        return payload


def test_lifecycle_states():

    agent = DemoAgent()

    lifecycle = AgentLifecycle()

    lifecycle.register(agent)

    assert lifecycle.state(agent) == "active"

    lifecycle.pause(agent)

    assert lifecycle.state(agent) == "paused"

    lifecycle.resume(agent)

    assert lifecycle.state(agent) == "active"

    lifecycle.stop(agent)

    assert lifecycle.state(agent) == "stopped"


def test_health_monitor():

    agent = DemoAgent()

    monitor = AgentHealthMonitor()

    health = monitor.check(agent)

    assert health["healthy"] is True


def test_metrics():

    metrics = AgentMetrics()

    metrics.record_success()

    metrics.record_failure()

    summary = metrics.summary()

    assert summary["executions"] == 2

    assert summary["failures"] == 1

    assert summary["successes"] == 1