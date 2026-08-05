"""
Intelligence Scheduler

Coordinates runtime scheduling.
"""

from .scheduler_state import SchedulerState


class IntelligenceScheduler:

    def __init__(self):

        self.state = SchedulerState()

    def start(self):

        self.state.start()

    def stop(self):

        self.state.stop()

    def status(self):

        return self.state.get_state()