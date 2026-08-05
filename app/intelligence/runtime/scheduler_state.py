"""
Scheduler State

Tracks runtime scheduler state.
"""

from datetime import UTC, datetime


class SchedulerState:

    def __init__(self):

        self.running = False

        self.started_at = None

    def start(self):

        self.running = True

        self.started_at = (
            datetime.now(UTC)
            .isoformat()
        )

    def stop(self):

        self.running = False

    def get_state(self):

        return {

            "running":
                self.running,

            "started_at":
                self.started_at

        }