from services.response_engine import ResponseEngine


def test_response_engine_containment():

    engine = ResponseEngine()


    result = engine.execute(

        {
            "decision":
                "contain_immediately",

            "priority":
                "critical",

            "actions":
                [
                    "isolate host",
                    "disable account"
                ]
        }

    )


    assert result["response_type"] == "containment"

    assert result["execution_state"] == "ready"

    assert result["metadata"]["automation"] is True



def test_response_engine_investigation():

    engine = ResponseEngine()


    result = engine.execute(

        {
            "decision":
                "investigate",

            "priority":
                "high",

            "actions":
                [
                    "collect logs"
                ]
        }

    )


    assert result["response_type"] == "investigation"

    assert result["metadata"]["approval_required"] is True



def test_response_engine_monitoring():

    engine = ResponseEngine()


    result = engine.execute(

        {
            "decision":
                "monitor",

            "priority":
                "low",

            "actions":
                [
                    "observe"
                ]
        }

    )


    assert result["response_type"] == "monitoring"

    assert result["execution_state"] == "planned"