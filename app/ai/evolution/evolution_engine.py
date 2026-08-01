from app.ai.evolution.evolution_database import EVOLUTION_DATABASE



def calculate_growth(
    career,
    completed_skills
):


    career_data = EVOLUTION_DATABASE.get(
        career,
        {}
    )


    required = career_data.get(
        "skills",
        []
    )


    completed = [
        skill.lower()
        for skill in completed_skills
    ]



    achieved = []

    remaining = []



    for skill in required:


        if skill in completed:

            achieved.append(skill)

        else:

            remaining.append(skill)



    if required:

        readiness = round(
            (len(achieved) / len(required))
            * 100
        )

    else:

        readiness = 0



    return {


        "career":

            career,


        "readiness_score":

            readiness,


        "skills_completed":

            achieved,


        "skills_remaining":

            remaining,


        "growth_status":

            "Improving"
            if readiness < 100
            else "Career Ready"


    }