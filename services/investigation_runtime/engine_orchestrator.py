import datetime
import uuid

from services.investigation_graph_runtime import InvestigationGraphRuntime

from services.cognitive_investigation_engine import (
    CognitiveInvestigationEngine,
)

from services.investigation_intelligence import (
    RiskReasoner,
    ConfidenceEngine,
    IntelligenceReport,
    AnalystSummary,
)


class EngineOrchestrator:
    """
    Sentinel DNA Investigation Engine Orchestrator.

    Coordinates:

    - Investigation Graph Runtime
    - Cognitive Investigation Engine
    - Investigation Intelligence Layer

    Produces autonomous SOC investigation output.
    """


    def __init__(self):

        self.graph_runtime = InvestigationGraphRuntime()

        self.cognitive_engine = CognitiveInvestigationEngine()


        # Investigation Intelligence Layer

        self.risk_reasoner = RiskReasoner()

        self.confidence_engine = ConfidenceEngine()

        self.report_engine = IntelligenceReport()

        self.analyst_summary = AnalystSummary()



    def normalize_event(
        self,
        event
    ):

        if isinstance(
            event,
            dict
        ):

            return event


        return {

            "id":
                f"INV-{uuid.uuid4().hex[:8].upper()}",

            "severity":
                "unknown",

            "description":
                event,

            "source":
                "autonomous_runtime"

        }



    def execute(
        self,
        event
    ):


        investigation_event = self.normalize_event(
            event
        )


        #
        # Investigation Graph Analysis
        #

        graph_result = self.graph_runtime.investigate(
            investigation_event
        )


        #
        # Cognitive Reasoning
        #

        if hasattr(
            self.cognitive_engine,
            "analyze"
        ):

            cognitive_result = self.cognitive_engine.analyze(
                investigation_event
            )

        else:

            cognitive_result = self.cognitive_engine.investigate(
                investigation_event
            )



        #
        # Unified intelligence context
        #

        intelligence_context = {

            "event":
                investigation_event,

            "graph":
                graph_result,

            "cognitive":
                cognitive_result

        }



        #
        # Risk Evaluation
        #

        risk = self.risk_reasoner.assess(
            intelligence_context
        )


        #
        # Confidence Evaluation
        #

        confidence = self.confidence_engine.evaluate(
            intelligence_context
        )


        #
        # Generate Intelligence Report
        #

        report = self.report_engine.generate(

            intelligence_context,

            risk,

            confidence

        )


        #
        # Analyst Summary
        #

        analyst_summary = self.analyst_summary.summarize(
            report
        )



        return {


            "engines_executed": [

                "Investigation Graph Runtime",

                "Cognitive Investigation Engine",

                "Investigation Intelligence",

                "Evidence Intelligence",

                "Threat Hunting",

                "Knowledge Graph",

                "Intelligence Fusion",

                "SOAR"

            ],


            "event":
                investigation_event,


            "graph_investigation":
                graph_result,


            "cognitive_analysis":
                cognitive_result,


            #
            # New AI SOC intelligence layer
            #

            "investigation_intelligence": {

                "risk":
                    risk,

                "confidence":
                    confidence,

                "report":
                    report,

                "analyst_summary":
                    analyst_summary

            },


            "status":
                "completed",


            "timestamp":
                datetime.datetime.now(
                    datetime.timezone.utc
                ).isoformat()

        }