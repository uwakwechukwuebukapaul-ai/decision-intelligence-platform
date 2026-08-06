"""
Sentinel DNA - AI Reasoning Engine

Combines intelligence signals into
SOC analyst reasoning.
"""


from .reasoning_schema import ReasoningResult
from .hypothesis_engine import HypothesisEngine
from .decision_engine import DecisionEngine
from .explanation_engine import ExplanationEngine




class ReasoningEngine:


    def __init__(self):

        self.hypothesis_engine = (
            HypothesisEngine()
        )

        self.decision_engine = (
            DecisionEngine()
        )

        self.explanation_engine = (
            ExplanationEngine()
        )



    def reason(
        self,
        intelligence: dict,
    ) -> dict:


        hypothesis = (
            self.hypothesis_engine.generate(
                intelligence
            )
        )


        actions = (
            self.decision_engine.decide(
                intelligence
            )
        )


        explanation = (
            self.explanation_engine.explain(
                intelligence,
                hypothesis
            )
        )


        result = ReasoningResult(

            indicator=
                intelligence.get(
                    "indicator",
                    "unknown"
                ),

            hypothesis=
                hypothesis["hypothesis"],

            confidence=
                hypothesis["confidence"],

            severity=
                intelligence.get(
                    "risk",
                    {}
                ).get(
                    "risk",
                    "unknown"
                ),

            analyst_summary=
                explanation,

            recommended_actions=
                actions,

            evidence=
                intelligence,

        )


        return result.to_dict()