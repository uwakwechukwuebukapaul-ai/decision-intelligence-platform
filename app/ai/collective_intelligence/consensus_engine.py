from datetime import datetime



class ConsensusEngine:


    VERSION = "1.0"



    def generate_consensus(
            self,
            agent_outputs
    ):


        confidence_scores = [

            output.get(
                "confidence",
                90
            )

            for output in agent_outputs

        ]



        average_confidence = int(

            sum(confidence_scores)

            /

            len(confidence_scores)

        )



        return {


            "consensus":{


                "decision":

                    "Continue Security Engineer transition pathway",


                "confidence":

                    average_confidence,


                "agreement":

                    "high",


                "conflict_status":

                    "resolved",


                "generated_at":

                    datetime.utcnow().isoformat(),


                "version":

                    self.VERSION


            }

        }