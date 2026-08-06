"""
Decision Intelligence Platform

Governance Registry

Enterprise governance layer for intelligence capabilities.

Responsible for:
- Capability ownership tracking
- Governance metadata management
- Policy attachment foundation
- Lifecycle governance
- Enterprise audit preparation
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict


# =====================================
# Governance Record
# =====================================

@dataclass
class GovernanceRecord:

    capability_name: str

    owner: str = "platform"

    category: str = "general"

    risk_level: str = "medium"

    compliance_status: str = "pending"

    policies: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )

    updated_at: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )


    # =================================
    # Policy Management
    # =================================

    def add_policy(
        self,
        policy: str
    ):

        if policy not in self.policies:

            self.policies.append(
                policy
            )

            self.updated_at = (
                datetime.now(UTC).isoformat()
            )


    # =================================
    # Serialization
    # =================================

    def to_dict(self):

        return {

            "capability_name":
                self.capability_name,

            "owner":
                self.owner,

            "category":
                self.category,

            "risk_level":
                self.risk_level,

            "compliance_status":
                self.compliance_status,

            "policies":
                self.policies,

            "metadata":
                self.metadata,

            "created_at":
                self.created_at,

            "updated_at":
                self.updated_at,

        }



# =====================================
# Governance Registry
# =====================================

class GovernanceRegistry:


    def __init__(self):

        self.records: Dict[
            str,
            GovernanceRecord
        ] = {}



    # =================================
    # Register Capability
    # =================================

    def register(
        self,
        capability_name: str,
        owner: str = "platform",
        category: str = "general",
        risk_level: str = "medium"
    ):

        if capability_name not in self.records:

            self.records[
                capability_name
            ] = GovernanceRecord(

                capability_name=capability_name,

                owner=owner,

                category=category,

                risk_level=risk_level

            )


        return self.records[
            capability_name
        ]



    # =================================
    # Exists
    # =================================

    def exists(
        self,
        capability_name: str
    ):

        return (
            capability_name
            in self.records
        )



    # =================================
    # Attach Policy
    # =================================

    def attach_policy(
        self,
        capability_name: str,
        policy: str
    ):

        record = self.register(
            capability_name
        )

        record.add_policy(
            policy
        )

        return record



    # =================================
    # Update Compliance
    # =================================

    def update_compliance(
        self,
        capability_name: str,
        status: str
    ):

        record = self.register(
            capability_name
        )

        record.compliance_status = status

        record.updated_at = (
            datetime.now(UTC).isoformat()
        )

        return record



    # =================================
    # Query
    # =================================

    def get(
        self,
        capability_name: str
    ):

        record = self.records.get(
            capability_name
        )

        if not record:

            return None


        return record.to_dict()



    def list_all(self):

        return [

            record.to_dict()

            for record
            in self.records.values()

        ]



# =====================================
# Global Governance Registry
# =====================================

governance_registry = (
    GovernanceRegistry()
)