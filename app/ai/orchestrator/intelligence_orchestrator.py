from datetime import datetime


from app.ai.orchestrator.decision_pipeline import (
    DecisionPipeline
)


from app.ai.orchestrator.orchestrator_memory import (
    OrchestratorMemory
)


from app.ai.orchestrator.pipeline_validator import (
    PipelineValidator
)



from app.ai.research.research_engine import (
    ResearchEngine
)


from app.ai.investment.investment_engine import (
    InvestmentEngine
)


from app.ai.executive.executive_advisor import (
    ExecutiveAdvisor
)



class IntelligenceOrchestrator:



    def __init__(self):

        self.research = ResearchEngine()

        self.investment = InvestmentEngine()

        self.executive = ExecutiveAdvisor()

        self.pipeline = DecisionPipeline()

        self.memory = OrchestratorMemory()

        self.validator = PipelineValidator()



    def analyze(
        self,
        question
    ):


        research_result = self.research.research(
            question
        )


        investment_result = self.investment.evaluate(
            question,
            {
                "market_score":
                    research_result["research"]["market_analysis"]["market_score"]
            }
        )


        executive_result = self.executive.advise(
            question,
            investment_result["investment_analysis"]
        )


        pipeline = self.pipeline.build(

            research_result,

            {
                "status":
                    "prediction integrated"
            },

            {
                "status":
                    "planning integrated"
            },

            {
                "status":
                    "execution integrated"
            },

            investment_result,

            executive_result

        )


        validation = self.validator.validate(
            pipeline
        )


        result = {


            "status":
                "completed",


            "decision_pipeline":
                pipeline,


            "validation":
                validation,


            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return result