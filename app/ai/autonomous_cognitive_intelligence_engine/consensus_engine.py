from datetime import datetime


class ConsensusEngine:


    def build_consensus(
        self,
        user_id,
        reasoning_result
    ):


        reasoning_level = reasoning_result.get(
            "reasoning_level",
            "basic"
        )


        if reasoning_level == "advanced":

            recommendation = (
                "Execute balanced autonomous strategy "
                "based on multi-layer intelligence consensus"
            )

            consensus_score = 98


        elif reasoning_level == "intermediate":

            recommendation = (
                "Proceed with monitored intelligence strategy"
            )

            consensus_score = 85


        else:

            recommendation = (
                "Collect additional intelligence before decision"
            )

            consensus_score = 70



        return {


            "user_id":

                user_id,


            "consensus_status":

                "completed",


            "consensus_score":

                consensus_score,


            "final_recommendation":

                recommendation,


            "consensus_factors":

                [

                    "Reasoning analysis",

                    "Engine availability",

                    "Decision confidence",

                    "Strategic alignment"

                ],


            "generated_at":

                datetime.utcnow().isoformat()

        }