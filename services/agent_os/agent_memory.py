class AgentMemory:
    """
    Persistent intelligence memory layer.

    Stores previous agent decisions,
    investigations and learned context.
    """


    def __init__(self):

        self.memory = []


    def remember(
        self,
        agent,
        information
    ):

        entry = {

            "agent":
                agent,

            "information":
                information

        }


        self.memory.append(
            entry
        )


        return entry


    def recall(
        self,
        agent=None
    ):

        if agent:

            return [

                item

                for item in self.memory

                if item["agent"] == agent

            ]


        return self.memory