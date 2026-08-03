class AgentMemory:


    def __init__(
        self,
        repository
    ):

        self.repository = repository



    def remember(
        self,
        agent_data
    ):


        return self.repository.save(

            "agent",

            agent_data

        )



    def get_agents(self):

        return self.repository.get(
            "agent"
        )