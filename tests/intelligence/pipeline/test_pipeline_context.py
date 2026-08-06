from app.intelligence.pipeline.pipeline_context import PipelineContext


def test_pipeline_context_creation():

    context = PipelineContext(
        capability="threat_intelligence"
    )

    assert context.capability == "threat_intelligence"

    assert context.payload == {}

    assert context.evidence == []

    assert context.findings == []

    assert context.completed_stages == []


def test_add_metadata():

    context = PipelineContext(
        capability="ioc_enrichment"
    )

    context.add_metadata(
        "severity",
        "high",
    )

    assert context.get_metadata(
        "severity"
    ) == "high"


def test_add_evidence():

    context = PipelineContext(
        capability="ioc_enrichment"
    )

    context.add_evidence(
        {"ip": "8.8.8.8"}
    )

    assert len(
        context.evidence
    ) == 1


def test_add_finding():

    context = PipelineContext(
        capability="ioc_enrichment"
    )

    context.add_finding(
        {
            "type": "ioc",
            "value": "malicious",
        }
    )

    assert len(
        context.findings
    ) == 1


def test_complete_stage():

    context = PipelineContext(
        capability="ioc_enrichment"
    )

    context.complete_stage(
        "Threat Intelligence"
    )

    assert context.completed_stages == [
        "Threat Intelligence"
    ]


def test_to_dict():

    context = PipelineContext(
        capability="threat_intelligence"
    )

    data = context.to_dict()

    assert data["capability"] == "threat_intelligence"

    assert "investigation_id" in data

    assert "created_at" in data