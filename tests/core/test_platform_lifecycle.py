from app.core import lifecycle, PlatformLifecycle


def test_lifecycle_startup():

    manager = PlatformLifecycle()

    manager.startup()

    assert manager.started is True



def test_lifecycle_health():

    manager = PlatformLifecycle()

    manager.startup()

    health = manager.health()

    assert health["lifecycle"] == "healthy"