from .agent_memory import AgentMemory


class AgentManager:


    def __init__(self):

        self.agents = {}

        self.memory = AgentMemory()



    def register_agent(
        self,
        name,
        agent
    ):

        self.agents[name] = agent



    def execute(
        self,
        agent_name,
        incident
    ):

        agent = self.agents.get(
            agent_name
        )


        if not agent:

            return {

                "agent": agent_name,

                "status": "missing"

            }


        result = agent.run(
            incident
        )


        self.memory.store(

            incident.get("incident_id"),

            agent_name,

            result

        )


        return result



    def execute_all(
        self,
        agents,
        incident
    ):

        results = []


        for agent in agents:

            results.append(

                self.execute(
                    agent,
                    incident
                )

            )


        return results