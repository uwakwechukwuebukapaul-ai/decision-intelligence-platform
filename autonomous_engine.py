"""
Sentinel DNA - Autonomous Investigation Engine

Core orchestration engine for autonomous security investigations.

Responsibilities:

- Start autonomous investigations
- Coordinate agents
- Collect evidence
- Generate investigation decisions
- Track execution lifecycle
"""


from __future__ import annotations


from datetime import datetime, timezone


from .investigation_agent import InvestigationAgent
from .agent_runtime import AgentRuntime
from .decision_manager import DecisionManager
from .approval_gate import ApprovalGate
from .execution_history import ExecutionHistory




class AutonomousEngine:
    """
    Main autonomous investigation controller.
    """


    def __init__(self):

        self.runtime = AgentRuntime()

        self.agent = InvestigationAgent()

        self.decision_manager = DecisionManager()

        self.approval_gate = ApprovalGate()

        self.history = ExecutionHistory()



    def investigate(
        self,
        indicator: str,
    ) -> dict:
        """
        Execute autonomous investigation workflow.
        """


        execution = self.runtime.create_execution(
            indicator
        )


        self.runtime.start_execution(
            execution["execution_id"]
        )


        investigation = self.agent.investigate(
            indicator
        )


        decision = self.decision_manager.evaluate(
            investigation
        )


        approval = self.approval_gate.check(
            decision
        )


        result = {

            "indicator": indicator,

            "execution": execution,

            "investigation": investigation,

            "decision": decision,

            "approval": approval,

            "status": "completed",

            "created_at": self.timestamp()

        }


        completed = self.runtime.complete_execution(
            execution["execution_id"],
            result,
        )


        self.history.record(
            completed
        )


        return completed




    def timestamp(self):

        return datetime.now(
            timezone.utc
        ).isoformat()