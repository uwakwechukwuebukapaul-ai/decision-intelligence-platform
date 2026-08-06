"""
Decision Intelligence Platform

Policy Engine

Governance decision layer for intelligence execution.

Responsible for:
- Capability execution authorization
- Risk policy evaluation
- Governance enforcement
- Future approval workflows
- Audit preparation

Enterprise purpose:
Controls autonomous intelligence actions
before execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict


# =====================================
# Policy Definition
# =====================================

@dataclass
class GovernancePolicy:

    name: str

    description: str = ""

    action: str = "allow"

    conditions: dict = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )


    def to_dict(self):

        return {

            "name":
                self.name,

            "description":
                self.description,

            "action":
                self.action,

            "conditions":
                self.conditions,

            "created_at":
                self.created_at,

        }



# =====================================
# Policy Evaluation Result
# =====================================

@dataclass
class PolicyDecision:

    allowed: bool

    action: str

    reason: str

    policy: str | None = None


    def to_dict(self):

        return {

            "allowed":
                self.allowed,

            "action":
                self.action,

            "reason":
                self.reason,

            "policy":
                self.policy,

        }



# =====================================
# Policy Engine
# =====================================

class PolicyEngine:


    def __init__(self):

        self.policies: Dict[
            str,
            GovernancePolicy
        ] = {}



    # =================================
    # Register Policy
    # =================================

    def register_policy(
        self,
        policy: GovernancePolicy
    ):

        self.policies[
            policy.name
        ] = policy

        return policy



    # =================================
    # Remove Policy
    # =================================

    def remove_policy(
        self,
        name: str
    ):

        return self.policies.pop(
            name,
            None
        )



    # =================================
    # Evaluate Execution
    # =================================

    def evaluate(
        self,
        capability_name: str,
        context: dict | None = None
    ):

        context = context or {}


        for policy in self.policies.values():


            if self._matches(
                policy,
                capability_name,
                context
            ):


                if policy.action == "deny":

                    return PolicyDecision(

                        allowed=False,

                        action="deny",

                        reason=
                            "Execution blocked by governance policy",

                        policy=policy.name

                    )



                if policy.action == "review":

                    return PolicyDecision(

                        allowed=False,

                        action="review",

                        reason=
                            "Execution requires approval",

                        policy=policy.name

                    )



        return PolicyDecision(

            allowed=True,

            action="allow",

            reason=
                "Execution permitted"

        )



    # =================================
    # Condition Matching
    # =================================

    def _matches(
        self,
        policy: GovernancePolicy,
        capability_name: str,
        context: dict
    ):


        conditions = policy.conditions


        if not conditions:

            return True



        if "capability" in conditions:

            if capability_name != conditions["capability"]:

                return False



        if "risk_level" in conditions:

            if context.get(
                "risk_level"
            ) != conditions["risk_level"]:

                return False



        if "user_role" in conditions:

            if context.get(
                "user_role"
            ) != conditions["user_role"]:

                return False



        return True



    # =================================
    # List Policies
    # =================================

    def list_policies(self):

        return [

            policy.to_dict()

            for policy
            in self.policies.values()

        ]



# =====================================
# Global Policy Engine
# =====================================

policy_engine = PolicyEngine()