"""
Sentinel DNA Base AI Agent

All investigation agents inherit from this class.
"""


from abc import ABC, abstractmethod
from datetime import datetime



class BaseAgent(ABC):


    def __init__(self, name):

        self.name = name

        self.created_at = datetime.utcnow()



    @abstractmethod
    def analyze(self, investigation):

        """
        Execute agent investigation logic.

        Must be implemented by child agents.
        """

        pass



    def status(self):

        return {

            "agent":
                self.name,

            "status":
                "READY",

            "created_at":
                self.created_at.isoformat()
        }