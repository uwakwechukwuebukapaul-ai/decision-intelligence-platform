from services.sentinel_core import SentinelCorePipeline



def test_sentinel_core_pipeline():


    engine = SentinelCorePipeline()


    result = engine.analyze(
        "Ransomware actor using PowerShell attacked finance database servers"
    )


    assert (
        result["status"]
        ==
        "sentinel_pipeline_completed"
    )


    assert (
        result["investigation"]["status"]
        ==
        "investigation_completed"
    )


    assert (
        "threat_intelligence"
        in
        result["intelligence"]
    )