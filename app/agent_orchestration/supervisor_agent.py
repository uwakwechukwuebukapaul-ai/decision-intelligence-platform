from .agent_manager import AgentManager
from .task_router import TaskRouter



class BasicAgent:


    def __init__(
        self,
        name
    ):

        self.name = name



    def run(
        self,
        incident
    ):

        return {

            "agent": self.name,

            "finding":
                f"{self.name} completed analysis",

            "indicator":
                incident.get("indicator")

        }



class SupervisorAgent:


    def __init__(self):

        self.router = TaskRouter()

        self.manager = AgentManager()


        self.register_default_agents()



    def register_default_agents(
        self
    ):

        agents = [

            "threat_agent",

            "detection_agent",

            "evidence_agent",

            "identity_agent"

        ]


        for agent in agents:

            self.manager.register_agent(

                agent,

                BasicAgent(agent)

            )



    def investigate(
        self,
        incident
    ):

        tasks = self.router.route(
            incident
        )


        results = self.manager.execute_all(

            tasks,

            incident

        )


        return {

            "incident_id":
                incident.get("incident_id"),

            "agents_used":
                tasks,

            "findings_count":
                len(results),

            "findings":
                results,

            "status":
                "completed"

        }