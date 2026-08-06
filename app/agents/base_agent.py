"""
Base AI Agent
"""


from datetime import datetime



class BaseAgent:


    def __init__(
        self,
        name,
        role
    ):

        self.name = name
        self.role = role



    def execute(
        self,
        context: dict
    ):

        return {

            "agent":
                self.name,

            "role":
                self.role,

            "status":
                "completed",

            "timestamp":
                datetime.utcnow().isoformat()

        }