"""
Runtime Job Queue
"""

from collections import deque


class JobQueue:

    def __init__(self):

        self._queue = deque()

    def enqueue(
        self,
        job,
    ):

        self._queue.append(
            job
        )

    def dequeue(self):

        if self._queue:

            return self._queue.popleft()

        return None

    def size(self):

        return len(
            self._queue
        )

    def is_empty(self):

        return (

            len(self._queue)

            == 0

        )