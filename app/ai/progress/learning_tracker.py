def calculate_skill_progress(
    current_skills,
    completed_skills
):

    current = [
        skill.lower()
        for skill in current_skills
    ]


    completed = [
        skill.lower()
        for skill in completed_skills
    ]


    total = len(current)


    if total == 0:

        return 0



    achieved = 0


    for skill in current:

        if skill in completed:

            achieved += 1



    progress = round(
        (achieved / total) * 100
    )


    return progress