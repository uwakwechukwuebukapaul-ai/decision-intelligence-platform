from app.intelligence.production_engine_loader import (
    load_production_engines
)


from app.intelligence.capability_registry import (
    capability_registry
)



def test_production_engines_loaded():

    result = load_production_engines()


    assert result["status"] == (
        "production engines loaded"
    )


    capabilities = (
        capability_registry.list_capabilities()
    )


    assert "reasoning" in capabilities

    assert "decision_core" in capabilities

    assert "forecasting" in capabilities

    assert "agent_execution" in capabilities



def test_registered_engine_manifest():

    manifest = (
        capability_registry.get_manifest(
            "reasoning"
        )
    )


    assert manifest is not None

    assert manifest.name == "reasoning"

    assert manifest.category == "cognitive"