"""
Sentinel DNA - AI Investigation Pipeline

Central coordinator for SOC investigations.

Flow:

IOC
 |
Intelligence
 |
Autonomous Investigation
 |
Case Creation
 |
Copilot
"""


from __future__ import annotations


from .pipeline_schema import InvestigationPipelineResult
from .pipeline_state import PipelineState


from app.intelligence.fusion import SentinelIntelligenceEngine
from app.intelligence.autonomous import AutonomousEngine
from app.cases.case_manager import CaseManager
from app.ai.copilot import CopilotEngine





class InvestigationPipeline:


    def __init__(self):

        self.intelligence = (
            SentinelIntelligenceEngine()
        )

        self.autonomous = (
            AutonomousEngine()
        )

        self.case_manager = (
            CaseManager()
        )

        self.copilot = (
            CopilotEngine()
        )



    def investigate(
        self,
        indicator: str,
    ):


        state = PipelineState()



        state.add(
            "start",
            "Investigation started"
        )



        intelligence_result = (
            self.intelligence
            .investigate(indicator)
        )


        state.add(
            "intelligence",
            "Threat intelligence completed"
        )



        autonomous_result = (
            self.autonomous
            .run(
                intelligence_result
            )
        )


        state.add(
            "autonomous",
            "Autonomous investigation completed"
        )



        case = (
            self.case_manager
            .create_case(
                indicator,
                intelligence_result
            )
        )


        state.add(
            "case",
            "SOC case created"
        )



        copilot = (
            self.copilot
            .assist(
                intelligence_result
            )
        )


        state.add(
            "copilot",
            "AI Copilot analysis generated"
        )



        result = InvestigationPipelineResult(

            indicator=indicator,

            status="completed",

            confidence=
            copilot.get(
                "confidence",
                0
            ),

            intelligence=intelligence_result,

            autonomous_result=autonomous_result,

            case=case,

            copilot=copilot,

        )


        output = result.to_dict()


        output["timeline"] = (
            state.history()
        )


        return output