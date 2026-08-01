def calculate_readiness(
    completed_skills,
    required_skills
):

    if not required_skills:
        return 0


    completed = 0


    for skill in required_skills:

        if skill.lower() in [
            s.lower()
            for s in completed_skills
        ]:
            completed += 1


    score = round(
        (completed / len(required_skills)) * 100
    )


    return score



def readiness_report(
    career,
    completed_skills,
    required_skills
):

    score = calculate_readiness(
        completed_skills,
        required_skills
    )


    missing = [

        skill

        for skill in required_skills

        if skill.lower()
        not in [
            s.lower()
            for s in completed_skills
        ]

    ]


    return {

        "career": career,

        "readiness_score": score,

        "completed_skills":
            completed_skills,

        "missing_skills":
            missing

    }