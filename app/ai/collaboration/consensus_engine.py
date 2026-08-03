from datetime import datetime
import uuid



class ConsensusEngine:


    def __init__(self):

        self.consensus_history = []



    def generate_consensus(
        self,
        mission_id,
        agent_outputs
    ):


        confidence = min(
            100,
            len(agent_outputs) * 30
        )


        recommendation = {

            "consensus_id":
                f"CONSENSUS-{uuid.uuid4().hex[:8].upper()}",


            "mission_id":
                mission_id,


            "agents":

                agent_outputs,


            "recommendation":

                "Proceed with strategic decision based on multi-agent analysis",


            "confidence":

                confidence,


            "status":

                "completed",


            "created_at":

                datetime.utcnow().isoformat()

        }


        self.consensus_history.append(
            recommendation
        )


        return recommendation




    def get_history(self):

        return {

            "count":
                len(self.consensus_history),


            "consensus":

                self.consensus_history

        }