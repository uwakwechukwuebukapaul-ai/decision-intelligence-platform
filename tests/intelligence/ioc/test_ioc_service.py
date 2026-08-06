from app.intelligence.ioc import IOCService



def test_ip_indicator():

    service = IOCService()


    result = service.lookup(
        "8.8.8.8"
    )


    assert result["type"] == "ip"

    assert result["risk_score"] == 0



def test_domain_indicator():

    service = IOCService()


    result = service.lookup(
        "example.com"
    )


    assert result["type"] == "domain"



def test_unknown_indicator():

    service = IOCService()


    result = service.lookup(
        "random-value"
    )


    assert result["type"] == "unknown"

    assert result["risk_score"] == 20