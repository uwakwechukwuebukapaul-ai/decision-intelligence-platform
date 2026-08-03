from app.ai.runtime.task_executor import TaskExecutor


class ExecutionManager:


    def __init__(self):

        self.executor = TaskExecutor()



    def execute_agents(
        self,
        agents,
        task
    ):


        results = []


        for agent in agents:

            results.append(

                self.executor.execute_task(
                    agent,
                    task
                )

            )


        return {

            "agents_executed":
                len(results),

            "results":
                results,

            "status":
                "completed"

        }