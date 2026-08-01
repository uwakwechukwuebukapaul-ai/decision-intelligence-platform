from app.knowledge.career_database import CAREER_DATABASE



def normalize_skills(skills):

    if not skills:
        return []

    return [
        skill.strip().lower()
        for skill in skills.split(",")
    ]



def calculate_match(user_skills, career):

    user_skill_list = normalize_skills(user_skills)

    required_skills = [
        skill.lower()
        for skill in career["skills"]
    ]


    matched = []

    missing = []


    for skill in required_skills:

        if skill in user_skill_list:

            matched.append(skill)

        else:

            missing.append(skill)



    if len(required_skills) == 0:

        score = 0

    else:

        score = round(
            (len(matched) / len(required_skills)) * 100
        )


    return {

        "score": score,

        "matched_skills": matched,

        "missing_skills": missing

    }



def analyze_profile(profile):


    results = []


    for career in CAREER_DATABASE:


        evaluation = calculate_match(
            profile.skills,
            career
        )


        results.append({

            "career": career["name"],

            "match_score": evaluation["score"],

            "description": career["description"],

            "matched_skills": evaluation["matched_skills"],

            "missing_skills": evaluation["missing_skills"],

            "certifications": career.get(
                "certifications",
                []
            )

        })



    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )



    recommendations = results[:3]



    top = recommendations[0]



    reasoning = f"""

{profile.name} is currently studying
{profile.education}.

The highest career match is
{top['career']} with a confidence score
of {top['match_score']}%.

The recommendation is based on:

Matched skills:
{', '.join(top['matched_skills'])}

Priority improvements:

{', '.join(top['missing_skills'])}

"""


    return {


        "user": profile.name,


        "profile": {

            "education": profile.education,

            "experience": profile.experience,

            "skills": profile.skills

        },


        "career_recommendations": recommendations,


        "skill_gap": top["missing_skills"],


        "certifications": top["certifications"],


        "ai_reasoning": reasoning,


        "engine_version":

        "Decision Intelligence Engine v3"

    }