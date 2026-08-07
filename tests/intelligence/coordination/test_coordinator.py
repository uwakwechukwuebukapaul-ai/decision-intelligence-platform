"""
Coordinator Tests

Tests intelligence workflow
orchestration.
"""

import pytest

from app.intelligence.coordination.coordinator import (
    Coordinator,
)

from app.intelligence.coordination.execution_plan import (
    ExecutionPlan,
)

from app.intelligence.runtime.job import (
    IntelligenceJob,
)


class FakeExecutor:
    """
    Mock intelligence runtime executor
    """

    def __init__(self):
        self.jobs = []

    def execute(self, job):
        self.jobs.append(job)

        return {
            "status": "completed",
            "capability": job.capability,
            "result": "success",
        }


@pytest.fixture
def executor():
    return FakeExecutor()


@pytest.fixture
def coordinator(executor):
    return Coordinator(
        executor=executor
    )


@pytest.fixture
def execution_plan():
    """
    Fake execution plan
    """

    class FakeStep:

        def __init__(
            self,
            name,
            capability,
            payload,
        ):
            self.name = name
            self.capability = capability
            self.payload = payload


    class FakePlan:

        def __init__(self):
            self.steps = [
                FakeStep(
                    "classification",
                    "threat_classification",
                    {
                        "ioc": "evil.com"
                    },
                ),
                FakeStep(
                    "risk",
                    "risk_scoring",
                    {
                        "severity": "high"
                    },
                ),
            ]

        def validate(self):
            return True


        def ordered_steps(self):
            return self.steps


    return FakePlan()


def test_coordinator_initialization(
    coordinator,
):
    """
    Coordinator initializes correctly
    """

    assert coordinator is not None

    assert coordinator.executor is not None


def test_execute_workflow(
    coordinator,
    execution_plan,
):
    """
    Coordinator executes execution plan
    """

    result = coordinator.execute(
        execution_plan
    )

    assert result is not None


def test_executor_receives_jobs(
    coordinator,
    execution_plan,
    executor,
):
    """
    Verify jobs are dispatched
    """

    coordinator.execute(
        execution_plan
    )

    assert len(
        executor.jobs
    ) == 2


def test_job_capabilities(
    coordinator,
    execution_plan,
    executor,
):
    """
    Verify correct capabilities
    """

    coordinator.execute(
        execution_plan
    )

    capabilities = [
        job.capability
        for job in executor.jobs
    ]

    assert (
        "threat_classification"
        in capabilities
    )

    assert (
        "risk_scoring"
        in capabilities
    )


def test_execution_result_structure(
    coordinator,
    execution_plan,
):
    """
    Verify investigation output
    """

    result = coordinator.execute(
        execution_plan
    )

    assert (
        "results"
        in result
    )


def test_invalid_plan_failure(
    coordinator,
):
    """
    Invalid plans should fail
    """

    class InvalidPlan:

        def validate(self):
            raise Exception(
                "Invalid execution plan"
            )


    with pytest.raises(Exception):

        coordinator.execute(
            InvalidPlan()
        )