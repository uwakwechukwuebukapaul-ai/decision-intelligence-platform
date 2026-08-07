"""
Context Aware Execution Tests
"""


from app.intelligence.runtime.bootstrap import (
    create_intelligence_runtime,
)

from app.intelligence.runtime.job import (
    IntelligenceJob,
)

from app.intelligence.context import (
    load_investigation_context,
)



def test_engine_receives_context():

    executor = create_intelligence_runtime()


    context = load_investigation_context(
        "INC-100"
    )


    result = executor.execute(

        IntelligenceJob(

            capability="risk_scoring",

            payload={},

            context=context,

        )

    )


    assert (
        result["status"]
        == "completed"
    )


    assert (
        result["result"]["case_id"]
        == "INC-100"
    )