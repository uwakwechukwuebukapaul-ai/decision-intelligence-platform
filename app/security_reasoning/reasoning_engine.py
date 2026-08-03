from datetime import datetime

from .context_builder import ContextBuilder
from .threat_reasoner import ThreatReasoner
from .risk_reasoner import RiskReasoner
from .evidence_reasoner import EvidenceReasoner
from .decision_engine import DecisionEngine
from .response_reasoner import ResponseReasoner
from .reasoning_memory import ReasoningMemory
from .reasoning_logger import ReasoningLogger



class SecurityReasoningEngine:


    def __init__(self):

        self.context = ContextBuilder()

        self.threat = ThreatReasoner()

        self.risk = RiskReasoner()

        self.evidence = EvidenceReasoner()

        self.decision = DecisionEngine()

        self.response = ResponseReasoner()

        self.memory = ReasoningMemory()

        self.logger = ReasoningLogger()



    def reason(self, event):

        context = self.context.build(event)

        threat = self.threat.analyze(context)

        risk = self.risk.calculate(threat)

        evidence = self.evidence.analyze(context)

        decision = self.decision.decide(
            risk,
            threat
        )

        response = self.response.recommend(
            decision
        )

        memory = self.memory.store(event)

        log = self.logger.log(event)


        return {

            "status":
                "completed",

            "event":
                event,

            "threat_analysis":
                threat,

            "risk_analysis":
                risk,

            "evidence":
                evidence,

            "decision":
                decision,

            "response":
                response,

            "memory":
                memory,

            "log":
                log,

            "created_at":
                datetime.utcnow().isoformat()

        }