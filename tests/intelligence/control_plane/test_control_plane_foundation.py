from app.intelligence.control_plane import (
    IntelligenceController,
    TaskManager,
    PolicyEngine,
    CapabilityManager,
    AuditLogger,
)



def build_controller():

    tasks = TaskManager()

    policy = PolicyEngine()

    capabilities = CapabilityManager()

    audit = AuditLogger()


    capabilities.register(
        "threat_analysis"
    )

    policy.allow_capability(
        "threat_analysis"
    )


    controller = IntelligenceController(
        tasks,
        policy,
        capabilities,
        audit,
    )


    return controller, audit



def test_control_plane_creates_task():

    controller, audit = build_controller()


    task = controller.submit(
        "threat_analysis",
        {
            "ioc": "example.com"
        }
    )


    assert task.status == "created"

    assert len(
        audit.history()
    ) == 1



def test_blocked_capability():

    controller, _ = build_controller()


    try:

        controller.submit(
            "malware_execution",
            {}
        )

        assert False


    except ValueError:

        assert True