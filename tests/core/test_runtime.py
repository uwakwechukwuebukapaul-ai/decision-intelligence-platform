from app.core import Container, IntelligenceRuntime



def test_runtime_start():

    container = Container()

    runtime = IntelligenceRuntime(
        container
    )

    runtime.start()

    status = runtime.health()

    assert status["runtime"] == "healthy"
    assert status["started"] is True



def test_runtime_stop():

    container = Container()

    runtime = IntelligenceRuntime(
        container
    )

    runtime.start()

    runtime.stop()

    assert runtime.started is False