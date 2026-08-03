from datetime import datetime


class ExecutionPlanner:


    def create_execution_plan(
        self,
        tasks
    ):


        execution = []


        priority = 1


        for task in tasks:

            execution.append({

                "task_id":
                    task["task_id"],

                "goal":
                    task["goal"],

                "priority":
                    priority,

                "dependency":
                    None if priority == 1 else "previous_task",

                "status":
                    "scheduled"

            })


            priority += 1



        return {

            "execution_plan":
                execution,

            "total_steps":
                len(execution),

            "created_at":
                datetime.utcnow().isoformat()

        }