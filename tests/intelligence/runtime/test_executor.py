"""
Runtime Executor Tests
"""

import pytest

from app.intelligence.runtime.registry import (
    CapabilityRegistry,
)

from app.intelligence.runtime.executor import (
    IntelligenceExecutor,
)

from app.intelligence.runtime.job import (
    IntelligenceJob,
)


class FakeEngine:

    def __init__(self):
        self.calls = []


    def execute(
        self,
        payload,
    ):

        self.calls.append(payload)

        return {
            "analysis": "complete"
        }


@pytest.fixture
def registry():

    registry = CapabilityRegistry()

    engine = FakeEngine()

    registry.register(
        "risk_scoring",
        engine,
    )

    return registry, engine



@pytest.fixture
def executor(registry):

    registry, _ = registry

    return IntelligenceExecutor(
        registry
    )



def test_capability_registration(
    registry,
):

    registry, _ = registry

    assert registry.has(
        "risk_scoring"
    )



def test_executor_runs_job(
    registry,
):

    registry, engine = registry


    executor = IntelligenceExecutor(
        registry
    )


    job = IntelligenceJob(
        capability="risk_scoring",
        payload={
            "severity": "high"
        },
    )


    result = executor.execute(
        job
    )


    assert result["status"] == "completed"

    assert len(
        engine.calls
    ) == 1



def test_unknown_capability(
    executor,
):

    job = IntelligenceJob(
        capability="unknown",
        payload={}
    )


    with pytest.raises(
        ValueError
    ):

        executor.execute(
            job
        )



def test_failed_execution(
    registry,
):

    class BrokenEngine:

        def execute(self, payload):
            raise Exception(
                "engine failed"
            )


    registry, _ = registry


    registry.register(
        "broken",
        BrokenEngine()
    )


    executor = IntelligenceExecutor(
        registry
    )


    result = executor.execute(
        IntelligenceJob(
            capability="broken",
            payload={}
        )
    )


    assert result["status"] == "failed"