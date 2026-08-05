from services.agent_os.agent_runtime import AgentRuntime


class TaskExecutor:
    """
    Executes AI agent tasks through the centralized Agent Runtime.
    """


    def __init__(self):

        self.runtime = AgentRuntime()



    def execute(
        self,
        agent,
        task
    ):

        return self.runtime.execute(
            agent,
            task
        )



    def history(
        self
    ):

        return self.runtime.history()