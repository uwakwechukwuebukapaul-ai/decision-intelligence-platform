SKILL_WEIGHTS = {

    "python": 10,

    "security": 10,

    "linux": 15,

    "siem": 20,

    "incident response": 20,

    "machine learning": 25,

    "cloud security": 25,

    "automation": 20,

    "threat intelligence": 20,

    "llm security": 25

}



def calculate_readiness(
        matched_skills,
        missing_skills
):

    score = 0


    for skill in matched_skills:

        score += SKILL_WEIGHTS.get(
            skill.lower(),
            5
        )


    max_score = (

        len(matched_skills)
        +
        len(missing_skills)

    )


    if max_score == 0:

        return 0


    readiness = round(

        (score /
        (
        score +
        sum(
            SKILL_WEIGHTS.get(
                skill.lower(),
                5
            )
            for skill in missing_skills
        )
        ))
        * 100

    )


    return readiness