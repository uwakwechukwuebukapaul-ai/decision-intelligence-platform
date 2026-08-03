from app.ai.runtime.agent_runtime import AgentRuntime


class TaskExecutor:


    def __init__(self):

        self.runtime = AgentRuntime()



    def execute_task(
        self,
        agent,
        task
    ):


        return self.runtime.execute(
            agent,
            task
        )