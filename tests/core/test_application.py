from app.core.application import runtime


def test_runtime_start():

    runtime.start()

    assert runtime.started is True



def test_runtime_health():

    runtime.start()

    result = runtime.health()

    assert result["runtime"] == "healthy"