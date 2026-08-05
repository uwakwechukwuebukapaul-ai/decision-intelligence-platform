"""
Job Registry

Stores runtime jobs.
"""


class JobRegistry:

    def __init__(self):

        self._jobs = {}

    def register(
        self,
        job,
    ):

        self._jobs[
            job.job_id
        ] = job

        return job

    def get(
        self,
        job_id,
    ):

        return self._jobs.get(
            job_id
        )

    def all_jobs(self):

        return [

            job.to_dict()

            for job in self._jobs.values()

        ]

    def count(self):

        return len(
            self._jobs
        )