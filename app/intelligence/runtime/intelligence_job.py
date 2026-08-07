"""
Sentinel DNA - Intelligence Job
"""

from datetime import datetime, UTC
from uuid import uuid4


class IntelligenceJob:

    def __init__(
        self,
        capability,
        payload=None,
    ):

        self.job_id = (
            f"JOB-{uuid4().hex[:8]}"
        )

        self.capability = capability

        self.payload = payload or {}

        self.status = "pending"

        self.result = None

        self.error = None

        self.created_at = datetime.now(UTC)

        self.completed_at = None


    def start(self):

        self.status = "running"


    def complete(
        self,
        result,
    ):

        self.status = "completed"

        self.result = result

        self.completed_at = datetime.now(UTC)


    def fail(
        self,
        error,
    ):

        self.status = "failed"

        self.error = str(error)

        self.completed_at = datetime.now(UTC)