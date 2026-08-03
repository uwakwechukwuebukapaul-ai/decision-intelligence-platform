from datetime import datetime


from app.ai.research.research_collector import (
    ResearchCollector
)


from app.ai.research.market_analyzer import (
    MarketAnalyzer
)


from app.ai.research.competitor_intelligence import (
    CompetitorIntelligence
)


from app.ai.research.evidence_store import (
    EvidenceStore
)


from app.ai.research.research_memory import (
    ResearchMemory
)



class ResearchEngine:



    def __init__(self):

        self.collector = ResearchCollector()

        self.market = MarketAnalyzer()

        self.competitor = CompetitorIntelligence()

        self.evidence = EvidenceStore()

        self.memory = ResearchMemory()



    def research(self, question):


        collected = self.collector.collect(
            question
        )


        evidence = collected["evidence"]


        market_analysis = self.market.analyze(
            evidence
        )


        competitor_analysis = self.competitor.analyze(
            question
        )


        self.evidence.store(
            collected
        )


        report = {


            "question":

                question,


            "evidence":

                evidence,


            "market_analysis":

                market_analysis,


            "competitor_analysis":

                competitor_analysis,


            "recommendation":

                "Proceed with AI SOC automation investment analysis",


            "confidence":

                85

        }


        self.memory.save(
            report
        )


        return {


            "status":

                "completed",


            "research":

                report,


            "timestamp":

                datetime.utcnow().isoformat()

        }