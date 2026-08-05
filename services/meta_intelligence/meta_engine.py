from .self_evaluation import SelfEvaluation
from .strategy_analysis import StrategyAnalysis
from .agent_intelligence import AgentIntelligence
from .optimization_engine import OptimizationEngine


class MetaEngine:
    """
    Sentinel DNA Meta Intelligence Layer.

    Higher-order intelligence system responsible for:

    - evaluating decisions
    - analysing strategies
    - monitoring agents
    - optimizing intelligence workflows
    """

    def __init__(self):

        self.evaluation = SelfEvaluation()

        self.strategy = StrategyAnalysis()

        self.agents = AgentIntelligence()

        self.optimizer = OptimizationEngine()


    def analyze(
        self,
        intelligence_context
    ):

        evaluation = self.evaluation.evaluate(
            intelligence_context
        )


        strategy = self.strategy.analyze(
            intelligence_context
        )


        agents = self.agents.inspect()


        optimization = self.optimizer.optimize(
            evaluation,
            strategy
        )


        return {

            "status": "meta_analysis_completed",

            "evaluation": evaluation,

            "strategy": strategy,

            "agents": agents,

            "optimization": optimization

        }