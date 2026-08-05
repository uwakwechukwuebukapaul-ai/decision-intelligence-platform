"""
Production Intelligence Engine Loader

Registers real platform capabilities
into the Intelligence Fabric.
"""


from app.intelligence.engine_loader import (
    engine_loader
)


from app.intelligence.adapters.reasoning_adapter import (
    reasoning_capability
)


from app.intelligence.adapters.decision_adapter import (
    decision_core_capability
)


from app.intelligence.adapters.forecasting_adapter import (
    forecasting_capability
)


from app.intelligence.adapters.agent_runtime_adapter import (
    agent_execution_capability
)




def load_production_engines():


    engine_loader.register_engine(

        name="reasoning",

        engine=reasoning_capability,

        description=
            "Autonomous reasoning intelligence",

        category=
            "cognitive"

    )


    engine_loader.register_engine(

        name="decision_core",

        engine=decision_core_capability,

        description=
            "Strategic decision intelligence",

        category=
            "decision"

    )


    engine_loader.register_engine(

        name="forecasting",

        engine=forecasting_capability,

        description=
            "Predictive intelligence forecasting",

        category=
            "prediction"

    )


    engine_loader.register_engine(

        name="agent_execution",

        engine=agent_execution_capability,

        description=
            "Autonomous agent execution",

        category=
            "agents"

    )


    return {

        "status":
            "production engines loaded"

    }