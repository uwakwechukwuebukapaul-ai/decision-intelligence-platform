from flask import Blueprint, request, jsonify


from app.ai.orchestrator.intelligence_orchestrator import (
    IntelligenceOrchestrator
)


from app.api.api_memory import (
    APIMemory
)



intelligence_api = Blueprint(
    "intelligence_api",
    __name__
)



engine = IntelligenceOrchestrator()

memory = APIMemory()



@intelligence_api.route(
    "/api/intelligence/analyze",
    methods=["POST"]
)

def analyze_intelligence():


    data = request.json


    question = data.get(
        "question"
    )


    if not question:

        return jsonify(

            {

                "error":
                    "Question required"

            }

        ),400



    result = engine.analyze(
        question
    )


    memory.store(
        {

            "question":
                question,


            "result":
                result

        }

    )


    return jsonify(result)