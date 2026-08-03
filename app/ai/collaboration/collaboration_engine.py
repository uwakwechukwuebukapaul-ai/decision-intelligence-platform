from app.ai.collaboration.team_manager import TeamManager
from app.ai.collaboration.agent_communication import AgentCommunication
from app.ai.collaboration.consensus_engine import ConsensusEngine



class CollaborationEngine:


    def __init__(self):

        self.team_manager = TeamManager()

        self.communication = AgentCommunication()

        self.consensus = ConsensusEngine()



    def execute_collaboration(
        self,
        mission_id,
        mission_title,
        agents,
        outputs
    ):


        team = self.team_manager.create_team(

            mission_title,

            mission_id,

            agents

        )


        for output in outputs:


            self.communication.send_message(

                output["agent"],

                "Consensus Engine",

                output["analysis"]

            )



        decision = self.consensus.generate_consensus(

            mission_id,

            outputs

        )


        return {


            "team":

                team,


            "consensus":

                decision

        }