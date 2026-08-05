from app.intelligence.engine_loader import engine_loader
from app.intelligence.capability_registry import capability_registry



def sample_engine(context):

    return {

        "message":
            "engine executed"

    }



def test_engine_registration():


    engine_loader.register_engine(

        "test_engine",

        sample_engine,

        "Testing intelligence registry",

        "testing"

    )


    assert (
        "test_engine"
        in capability_registry.list_capabilities()
    )



def test_engine_execution():


    result = capability_registry.execute(

        "test_engine",

        {}

    )


    assert result["message"] == "engine executed"