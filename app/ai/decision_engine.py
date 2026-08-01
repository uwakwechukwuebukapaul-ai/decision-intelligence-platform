from app.knowledge.career_database import CAREER_DATABASE



def calculate_match(user_skills, career_skills):

    score = 0

    user_skills = [
        skill.strip().lower()
        for skill in user_skills.split(",")
    ]


    for skill in career_skills:

        if skill.lower() in user_skills:

            score += 1


    return score



def analyze_profile(profile):

    user_skills = profile.skills or ""


    career_results = []


    for career in CAREER_DATABASE:

        score = calculate_match(
            user_skills,
            career["skills"]
        )


        career_results.append({

            "career": career["name"],

            "match_score": score,

            "description": career["description"]

        })


    career_results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )


    recommendations = career_results[:3]


    return {


        "user": profile.name,


        "current_profile": {

            "education": profile.education,

            "experience": profile.experience,

            "skills": profile.skills,

            "goals": profile.goals

        },


        "career_recommendations": recommendations,


        "skill_gap": [

            "Advanced technical skills",

            "Industry certifications",

            "Real-world projects"

        ],


        "next_steps": [

            "Build portfolio projects",

            "Develop professional network",

            "Gain practical experience"

        ],


        "engine_version": "Decision Intelligence Engine v2"

    }