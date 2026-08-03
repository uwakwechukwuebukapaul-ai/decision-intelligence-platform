from datetime import datetime
import uuid


class ActionManager:


    def create_actions(
        self,
        tasks
    ):

        actions = []


        for task in tasks:

            actions.append({

                "action_id":
                    "ACTION-" + str(uuid.uuid4())[:8].upper(),

                "task_id":
                    task["task_id"],

                "objective":
                    task["goal"],

                "status":
                    "ready",

                "created_at":
                    datetime.utcnow().isoformat()

            })


        return {

            "actions":
                actions,

            "count":
                len(actions)

        }