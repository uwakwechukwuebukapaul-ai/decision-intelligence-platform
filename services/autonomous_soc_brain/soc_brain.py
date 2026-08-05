from .reasoning_engine import ReasoningEngine
from .agent_coordinator import AgentCoordinator
from .investigation_planner import InvestigationPlanner
from .risk_decision import RiskDecision
from .memory_manager import MemoryManager


class AutonomousSOCBrain:
    """
    Central AI reasoning layer for Sentinel DNA SOC operations.
    """

    def __init__(self):

        self.reasoning = ReasoningEngine()
        self.coordinator = AgentCoordinator()
        self.planner = InvestigationPlanner()
        self.risk = RiskDecision()
        self.memory = MemoryManager()


    def investigate(self, event):

        context = self.reasoning.analyze(event)

        agents = self.coordinator.select_agents(
            context
        )

        plan = self.planner.create_plan(
            context
        )

        decision = self.risk.evaluate(
            context
        )

        self.memory.store(
            event,
            decision
        )

        return {
            "event": event,
            "context": context,
            "agents": agents,
            "plan": plan,
            "decision": decision
        }