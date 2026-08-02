from datetime import datetime


class GoalMemory:
    """
    Stores autonomous goal history.
    """

    def __init__(self):

        self.memory = []

        self.version = "1.0"



    def store_goal(self, goal):


        entry = {


            "goal":
                goal,


            "stored_at":
                datetime.utcnow().isoformat()


        }


        self.memory.append(entry)


        return {


            "memory_status":
                "stored",


            "total_goals":
                len(self.memory),


            "latest_goal":
                entry,


            "version":
                self.version

        }