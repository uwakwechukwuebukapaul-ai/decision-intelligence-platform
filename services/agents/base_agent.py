from abc import ABC, abstractmethod
from datetime import datetime, timezone


class BaseAgent(ABC):
    """
    Base contract for all Sentinel DNA AI agents.
    """


    def __init__(
        self,
        name
    ):

        self.name = name


    def timestamp(self):

        return datetime.now(
            timezone.utc
        ).isoformat()


    @abstractmethod
    def execute(
        self,
        context
    ):

        pass