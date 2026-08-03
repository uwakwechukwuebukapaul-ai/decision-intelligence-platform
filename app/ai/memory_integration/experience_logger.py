from datetime import datetime



class ExperienceLogger:


    def log(

        self,

        agent_results

    ):

        experiences = []


        for result in agent_results:


            experiences.append({

                "agent":
                    result.get(
                        "agent"
                    ),

                "experience":
                    result.get(
                        "output"
                    ),

                "timestamp":
                    datetime.utcnow().isoformat()

            })


        return {

            "count":
                len(experiences),

            "experiences":
                experiences

        }