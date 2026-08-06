from app.intelligence.kernel.service_factory import ServiceFactory


def test_factory_creates_services():

    services = ServiceFactory.create()

    assert services is not None