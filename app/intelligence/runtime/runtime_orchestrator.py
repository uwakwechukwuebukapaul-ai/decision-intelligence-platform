"""
Runtime Orchestrator

Coordinates runtime execution.
"""

from .job_queue import JobQueue
from .job_registry import JobRegistry


class RuntimeOrchestrator:

    def __init__(self):

        self.registry = JobRegistry()

        self.queue = JobQueue()

    def submit(
        self,
        job,
    ):

        self.registry.register(
            job
        )

        self.queue.enqueue(
            job
        )

        return job.to_dict()

    def next_job(self):

        return self.queue.dequeue()

    def queue_size(self):

        return self.queue.size()

    def registered_jobs(self):

        return self.registry.all_jobs()