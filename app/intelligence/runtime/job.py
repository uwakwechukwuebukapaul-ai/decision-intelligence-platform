"""
Runtime Job

Represents a single intelligence execution task.
"""

from datetime import UTC, datetime
import uuid


class IntelligenceJob:

    def __init__(
        self,
        capability: str,
        payload: dict | None = None,
    ):

        self.job_id = str(
            uuid.uuid4()
        )

        self.capability = capability

        self.payload = payload or {}

        self.status = "queued"

        self.created_at = (
            datetime.now(UTC)
            .isoformat()
        )

    def start(self):

        self.status = "running"

    def complete(self):

        self.status = "completed"

    def fail(self):

        self.status = "failed"

    def cancel(self):

        self.status = "cancelled"

    def to_dict(self):

        return {

            "job_id":
                self.job_id,

            "capability":
                self.capability,

            "payload":
                self.payload,

            "status":
                self.status,

            "created_at":
                self.created_at

        }