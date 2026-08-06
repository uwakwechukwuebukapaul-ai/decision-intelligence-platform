"""
Decision Intelligence Platform

Governance Middleware

Central enforcement layer between
intelligence execution requests and
capability execution.

Enterprise responsibilities:
- Policy enforcement
- Governance decision checks
- Capability authorization
- Audit foundation
- Execution safety controls
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC


from app.intelligence.governance.policy_engine import (
    policy_engine
)


from app.intelligence.governance.governance_registry import (
    governance_registry
)


from app.intelligence.governance.capability_health import (
    capability_health_manager
)



# =====================================
# Governance Decision
# =====================================

@dataclass
class GovernanceDecision:

    allowed: bool

    capability: str

    reason: str

    timestamp: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )


    def to_dict(self):

        return {

            "allowed":
                self.allowed,

            "capability":
                self.capability,

            "reason":
                self.reason,

            "timestamp":
                self.timestamp

        }



# =====================================
# Governance Middleware
# =====================================

class GovernanceMiddleware:


    """
    Controls intelligence execution flow.

    Every capability execution should
    pass through this layer.
    """



    def __init__(self):

        self.audit_log = []



    # =================================
    # Authorization Check
    # =================================

    def authorize(
        self,
        capability: str,
        context: dict | None = None
    ):

        context = context or {}


        decision = policy_engine.evaluate(

            capability,

            context

        )


        governance_registry.record_decision(

            capability,

            decision

        )


        self.audit_log.append(

            decision

        )


        return decision



    # =================================
    # Execute Wrapper
    # =================================

    def execute(

        self,

        capability: str,

        executor,

        context: dict | None = None

    ):


        decision = self.authorize(

            capability,

            context

        )


        if not decision.allowed:


            return {

                "status":
                    "blocked",

                "reason":
                    decision.reason,

                "governance":
                    decision.to_dict()

            }



        try:


            result = executor()



            capability_health_manager.record_success(

                capability

            )


            return {

                "status":
                    "success",

                "result":
                    result,

                "governance":
                    decision.to_dict()

            }



        except Exception as exc:


            capability_health_manager.record_failure(

                capability,

                str(exc)

            )


            return {

                "status":
                    "error",

                "message":
                    str(exc),

                "governance":
                    decision.to_dict()

            }



    # =================================
    # Audit Retrieval
    # =================================

    def get_audit_events(
        self
    ):

        return [

            event.to_dict()

            for event
            in self.audit_log

        ]



# =====================================
# Global Middleware
# =====================================

governance_middleware = (
    GovernanceMiddleware()
)