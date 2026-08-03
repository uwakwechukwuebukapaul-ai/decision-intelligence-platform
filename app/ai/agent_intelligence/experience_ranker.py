from datetime import datetime


class ExperienceRanker:


    """
    Calculates agent capability score
    """



    def calculate_score(
        self,
        profile
    ):


        success_score = (

            profile.get(
                "success_rate",
                0
            )
            *
            0.6

        )


        mission_score = min(

            profile.get(
                "missions_completed",
                0
            )
            *
            2,

            100

        ) * 0.2



        expertise_score = (

            len(
                profile.get(
                    "domains",
                    []
                )
            )
            *
            20

        ) * 0.2



        total = round(

            success_score
            +
            mission_score
            +
            expertise_score,

            2

        )


        return {

            "agent_id":
                profile["agent_id"],


            "experience_score":
                total,


            "timestamp":
                datetime.utcnow().isoformat()

        }