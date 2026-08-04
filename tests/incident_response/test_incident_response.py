from services.incident_response import IncidentResponseEngine



def test_incident_response_engine():

    engine = IncidentResponseEngine()


    result = engine.respond(
        "Ransomware actor using PowerShell attacked finance database servers"
    )


    assert (
        result["status"]
        ==
        "incident_response_completed"
    )


    assert (
        "isolate_host"
        in
        result["actions"]
    )


    assert (
        len(result["execution"])
        >
        0
    )