"""
Runtime Orchestrator

Coordinates runtime execution.
"""

from .job_queue import JobQueue
from .job_registry import JobRegistry
from .execution_engine import ExecutionEngine
from .worker import Worker


class RuntimeOrchestrator:

    def __init__(self):

        self.registry = JobRegistry()

        self.queue = JobQueue()

        self.engine = ExecutionEngine()

        self.worker = Worker(
            self.engine
        )

    def submit(
        self,
        job,
    ):

        self.registry.register(job)

        self.queue.enqueue(job)

        return job.to_dict()

    def execute(
        self,
        job,
    ):

        self.registry.register(job)

        return self.worker.run(job)

    def next_job(self):

        return self.queue.dequeue()

    def queue_size(self):

        return self.queue.size()

    def registered_jobs(self):

        return self.registry.all_jobs()