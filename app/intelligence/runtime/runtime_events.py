"""
Runtime Events

Enterprise runtime event stream.
"""

from __future__ import annotations

from datetime import UTC, datetime


class RuntimeEvents:

    JOB_CREATED = "JOB_CREATED"

    JOB_STARTED = "JOB_STARTED"

    JOB_COMPLETED = "JOB_COMPLETED"

    JOB_FAILED = "JOB_FAILED"

    JOB_CANCELLED = "JOB_CANCELLED"

    def __init__(self):

        self._events = []

    def emit(
        self,
        event: str,
        execution_id: str,
        details: dict | None = None,
    ) -> dict:

        record = {

            "event": event,

            "execution_id": execution_id,

            "details": details or {},

            "timestamp": datetime.now(
                UTC
            ).isoformat(),
        }

        self._events.append(record)

        return record

    def all_events(self):

        return list(self._events)

    def clear(self):

        self._events.clear()

    def count(self):

        return len(self._events)