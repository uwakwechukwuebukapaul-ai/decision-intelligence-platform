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
- Compliance event tracking
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


from app.intelligence.governance.governance_audit import (
    governance_audit
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

    Every capability execution passes
    through governance validation.
    """


    def __init__(self):

        self.audit_log = []



    # =================================
    # Authorization
    # =================================

    def authorize(

        self,

        capability: str,

        context: dict | None = None

    ):


        context = context or {}


        policy_result = policy_engine.evaluate(

            capability,

            context

        )


        if hasattr(
            policy_result,
            "allowed"
        ):

            allowed = policy_result.allowed

            reason = getattr(

                policy_result,

                "reason",

                "Policy evaluation completed"

            )


        elif isinstance(

            policy_result,

            dict

        ):

            allowed = policy_result.get(

                "allowed",

                False

            )

            reason = policy_result.get(

                "reason",

                "Policy evaluation completed"

            )


        else:

            allowed = False

            reason = (
                "Invalid policy response"
            )



        decision = GovernanceDecision(

            allowed=allowed,

            capability=capability,

            reason=reason

        )



        governance_registry.record_decision(

            capability,

            decision

        )



        self.audit_log.append(

            decision

        )



        governance_audit.record(

            capability=capability,

            action="authorization",

            decision=(

                "allowed"

                if allowed

                else "blocked"

            ),

            user_id=context.get(

                "user_id"

            ),

            objective=context.get(

                "objective"

            ),

            reason=reason

        )



        return decision



    # =================================
    # Evaluation Interface
    # =================================

    def evaluate(

        self,

        capability: str,

        context: dict | None = None,

        **kwargs

    ):


        context = context or {}


        context.update(

            kwargs

        )


        decision = self.authorize(

            capability,

            context

        )


        # API compatibility layer.
        # Existing execution routes
        # expect dictionary responses.

        return {

            "allowed":

                decision.allowed,

            "capability":

                decision.capability,

            "reason":

                decision.reason,

            "timestamp":

                decision.timestamp

        }



    # =================================
    # Execution Wrapper
    # =================================

    def execute(

        self,

        capability: str,

        executor,

        context: dict | None = None

    ):


        context = context or {}


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



            governance_audit.record(

                capability=capability,

                action="execution",

                decision="success",

                user_id=context.get(

                    "user_id"

                ),

                objective=context.get(

                    "objective"

                )

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



            governance_audit.record(

                capability=capability,

                action="execution",

                decision="error",

                user_id=context.get(

                    "user_id"

                ),

                objective=context.get(

                    "objective"

                ),

                reason=str(exc)

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