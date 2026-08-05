"""
Audit Manager

Tracks control plane activities.
"""

from datetime import UTC, datetime


class AuditManager:
    def __init__(self):
        self.events = []

    def log(self, action, actor="system"):
        event = {
            "action": action,
            "actor": actor,
            "timestamp": datetime.now(UTC).isoformat(),
        }

        self.events.append(event)
        return event

    def get_events(self):
        return self.events