"""
Sentinel DNA - Result Aggregator Tests

Validates that investigation agent outputs
are converted into unified intelligence reports.
"""

from app.ai.investigation_orchestrator.result_aggregator import (
    InvestigationResultAggregator,
)

from app.investigations.investigation import Investigation



def test_result_aggregator_creates_report():

    investigation = Investigation(
        investigation_id="TEST-001",
        case_id="INC-TEST-001",
    )


    investigation.state.set_risk_score(
        85
    )


    investigation.state.set_confidence_score(
        0.92
    )


    investigation.state.set_classification(
        "PHISHING_ATTACK"
    )


    investigation.add_finding(
        {
            "type": "IOC",
            "value": "malicious-domain.com",
        }
    )


    investigation.state.add_recommendation(
        "Block malicious domain"
    )


    aggregator = InvestigationResultAggregator()


    report = aggregator.aggregate(
        investigation
    )


    assert report["investigation_id"] == "TEST-001"

    assert report["severity"] == "CRITICAL"

    assert report["risk_score"] == 85

    assert report["confidence"] == 0.92

    assert report["classification"] == "PHISHING_ATTACK"

    assert len(report["findings"]) == 1

    assert len(report["recommendations"]) == 1