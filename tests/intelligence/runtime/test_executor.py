"""
Tests for Intelligence Executor
"""

from app.intelligence.runtime import IntelligenceJob
from app.intelligence.runtime.executor import IntelligenceExecutor


def threat_handler(payload):

    return {
        "analysis":
            "Threat intelligence completed",
        "payload":
            payload
    }



def test_executor_success():

    executor = IntelligenceExecutor()


    executor.register_capability(
        "threat_intelligence",
        threat_handler
    )


    job = IntelligenceJob(
        "threat_intelligence",
        {
            "ioc":
                "example.com"
        }
    )


    result = executor.execute(
        job
    )


    assert result["status"] == "completed"

    assert job.status == "completed"



def test_executor_unknown_capability():

    executor = IntelligenceExecutor()


    job = IntelligenceJob(
        "unknown_capability"
    )


    result = executor.execute(
        job
    )


    assert result["status"] == "failed"

    assert job.status == "failed"