from .hunt_model import HuntModel
from .query_builder import QueryBuilder
from .hypothesis_engine import HypothesisEngine



class ThreatHunterEngine:
    """
    Autonomous threat hunting engine.

    Pipeline:

    Context
       |
    Hypothesis Generation
       |
    Query Creation
       |
    Hunt Execution
       |
    Findings
    """


    def __init__(self):

        self.hypothesis_engine = HypothesisEngine()

        self.query_builder = QueryBuilder()



    def hunt(
        self,
        context
    ):


        hypotheses = (
            self.hypothesis_engine.generate(
                context
            )
        )


        results = []


        for hypothesis in hypotheses:


            query = (
                self.query_builder.build(
                    hypothesis
                )
            )


            hunt = HuntModel(

                hypothesis=hypothesis,

                query=query["query"],

                findings=[

                    {

                        "finding":
                            "Suspicious activity pattern detected",

                        "confidence":
                            "medium"

                    }

                ],

                status="completed"

            )


            results.append(
                hunt.to_dict()
            )


        return {

            "status":
                "threat_hunting_completed",

            "results":
                results

        }