"""
Decision Intelligence Platform

Capability Health Management

Tracks intelligence capability runtime health,
execution statistics, failures, and availability.

Enterprise purpose:
- Capability observability
- Runtime reliability tracking
- Engine health monitoring
- Governance foundation
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Dict
from threading import RLock



# =====================================
# Capability Health Record
# =====================================

@dataclass
class CapabilityHealth:

    name: str

    status: str = "unknown"

    executions: int = 0

    failures: int = 0

    last_execution: str | None = None

    last_error: str | None = None

    created_at: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )

    updated_at: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )


    # =================================
    # Metrics
    # =================================

    @property
    def success_count(self):

        return max(
            self.executions - self.failures,
            0
        )


    @property
    def success_rate(self):

        if self.executions == 0:
            return 100.0

        return round(
            (
                self.success_count /
                self.executions
            ) * 100,
            2
        )


    @property
    def failure_rate(self):

        if self.executions == 0:
            return 0.0

        return round(
            (
                self.failures /
                self.executions
            ) * 100,
            2
        )


    # =================================
    # State Evaluation
    # =================================

    def evaluate_status(self):

        if self.executions == 0:

            self.status = "healthy"

        elif self.failure_rate >= 50:

            self.status = "unavailable"

        elif self.failure_rate >= 10:

            self.status = "degraded"

        else:

            self.status = "healthy"



    # =================================
    # Execution Events
    # =================================

    def mark_success(self):

        self.executions += 1

        self.last_execution = (
            datetime.now(UTC).isoformat()
        )

        self.updated_at = (
            datetime.now(UTC).isoformat()
        )

        self.evaluate_status()



    def mark_failure(
        self,
        error: str
    ):

        self.executions += 1

        self.failures += 1

        self.last_execution = (
            datetime.now(UTC).isoformat()
        )

        self.last_error = error

        self.updated_at = (
            datetime.now(UTC).isoformat()
        )

        self.evaluate_status()



    # =================================
    # Serialization
    # =================================

    def to_dict(self):

        return {

            "name":
                self.name,

            "status":
                self.status,

            "executions":
                self.executions,

            "failures":
                self.failures,

            "success_count":
                self.success_count,

            "success_rate":
                self.success_rate,

            "failure_rate":
                self.failure_rate,

            "last_execution":
                self.last_execution,

            "last_error":
                self.last_error,

            "created_at":
                self.created_at,

            "updated_at":
                self.updated_at

        }



# =====================================
# Health Manager
# =====================================

class CapabilityHealthManager:


    def __init__(self):

        self.health_records: Dict[
            str,
            CapabilityHealth
        ] = {}

        # Reentrant lock prevents nested lock deadlocks
        self.lock = RLock()



    # =================================
    # Register Capability
    # =================================

    def register(
        self,
        capability_name: str
    ):

        with self.lock:

            if capability_name not in self.health_records:

                self.health_records[
                    capability_name
                ] = CapabilityHealth(

                    name=capability_name,

                    status="healthy"

                )


            return self.health_records[
                capability_name
            ]



    # =================================
    # Record Success
    # =================================

    def record_success(
        self,
        capability_name: str
    ):

        with self.lock:

            health = self.register(
                capability_name
            )

            health.mark_success()

            return health.to_dict()



    # =================================
    # Record Failure
    # =================================

    def record_failure(
        self,
        capability_name: str,
        error: str
    ):

        with self.lock:

            health = self.register(
                capability_name
            )

            health.mark_failure(
                error
            )

            return health.to_dict()



    # =================================
    # Query
    # =================================

    def get_health(
        self,
        capability_name: str
    ):

        with self.lock:

            health = self.health_records.get(
                capability_name
            )

            if not health:

                return None


            return health.to_dict()



    def list_health(self):

        with self.lock:

            return [

                health.to_dict()

                for health
                in self.health_records.values()

            ]



# =====================================
# Global Governance Component
# =====================================

capability_health_manager = (
    CapabilityHealthManager()
)