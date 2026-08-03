from datetime import datetime
import uuid


class AgentProfile:

    """
    Agent Experience Profile

    Stores:
    - Agent history
    - Mission performance
    - Domain expertise
    """


    def __init__(self):

        self.agents = {}



    def create_profile(
        self,
        agent_id,
        domain
    ):

        profile = {

            "profile_id":
                f"PROFILE-{uuid.uuid4().hex[:8].upper()}",


            "agent_id":
                agent_id,


            "domains":
                [domain],


            "missions_completed":
                0,


            "successful_missions":
                0,


            "success_rate":
                0,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.agents[agent_id] = profile


        return profile



    def update_experience(
        self,
        agent_id,
        success
    ):


        if agent_id not in self.agents:

            return {

                "status":
                    "agent_not_found"

            }


        profile = self.agents[agent_id]


        profile["missions_completed"] += 1


        if success:

            profile["successful_missions"] += 1



        profile["success_rate"] = round(

            (
                profile["successful_missions"]
                /
                profile["missions_completed"]
            )
            *
            100,

            2

        )


        return profile



    def get_profile(
        self,
        agent_id
    ):

        return self.agents.get(
            agent_id
        )