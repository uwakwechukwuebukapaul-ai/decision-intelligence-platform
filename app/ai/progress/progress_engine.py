from app.knowledge.career_database import CAREER_DATABASE


def normalize_skills(skills):

    if not skills:
        return []

    return [
        skill.strip().lower()
        for skill in skills.split(",")
    ]



def calculate_readiness(
    career,
    user_skills
):

    user_skills = normalize_skills(
        user_skills
    )


    required = career.get(
        "skills",
        []
    )


    completed = []
    missing = []


    for skill in required:

        if skill.lower() in user_skills:

            completed.append(
                skill
            )

        else:

            missing.append(
                skill
            )



    if required:

        score = round(
            (len(completed) /
            len(required))
            * 100
        )

    else:

        score = 0



    return {

        "readiness_score": score,

        "completed_skills": completed,

        "missing_skills": missing

    }



def generate_progress(
    target_career,
    user_skills
):


    selected = None


    for career in CAREER_DATABASE:

        if career["name"] == target_career:

            selected = career
            break



    if not selected:


        return {

            "error":
            "Career not found"

        }



    result = calculate_readiness(

        selected,

        user_skills

    )



    return {

        "career":
        target_career,

        **result,

        "engine_version":
        "Progress Intelligence Engine v1"

    }