from datetime import datetime
import uuid


class TaskGenerator:


    def generate(
        self,
        goals
    ):

        tasks = []


        for goal in goals:

            tasks.append({

                "task_id":
                    "TASK-" + str(uuid.uuid4())[:8].upper(),

                "goal":
                    goal,

                "status":
                    "pending"

            })


        return {

            "tasks":
                tasks,

            "task_count":
                len(tasks),

            "created_at":
                datetime.utcnow().isoformat()

        }