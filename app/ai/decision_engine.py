from app.knowledge.career_database import CAREER_DATABASE



def normalize_skills(skills):

    if not skills:

        return []


    return [
        skill.strip().lower()
        for skill in skills.split(",")
    ]




def calculate_skill_score(
        user_skills,
        career_skills
):

    score = 0


    for skill in career_skills:

        if skill.lower() in user_skills:

            score += 10


    return score




def calculate_education_score(
        education,
        career
):

    if not education:

        return 0


    education = education.lower()


    if "cyber" in education:

        if career["category"] in [
            "Cybersecurity Operations",
            "Cybersecurity Engineering",
            "Cyber Threat Intelligence",
            "Incident Investigation"
        ]:

            return 20


    if "ai" in education:

        if career["category"] == "Artificial Intelligence Security":

            return 20


    return 5




def calculate_experience_score(
        experience
):

    if not experience:

        return 0


    experience = experience.lower()


    if "student" in experience:

        return 10


    if "professional" in experience:

        return 15


    return 5




def calculate_demand_score(
        demand
):

    scores = {

        "Very High": 15,

        "High": 12,

        "Medium": 8,

        "Emerging": 10

    }


    return scores.get(
        demand,
        5
    )




def generate_reason(
        profile,
        career
):

    reasons = []


    if profile.education:

        reasons.append(
            f"{profile.education} background aligns with {career['category']}."
        )


    reasons.append(
        f"Your skills match important requirements for {career['name']}."
    )


    reasons.append(
        f"Market demand level: {career['demand']}."
    )


    return reasons




def analyze_profile(profile):


    user_skills = normalize_skills(
        profile.skills
    )


    career_results = []



    for career in CAREER_DATABASE:


        skill_score = calculate_skill_score(
            user_skills,
            career["skills"]
        )


        education_score = calculate_education_score(
            profile.education,
            career
        )


        experience_score = calculate_experience_score(
            profile.experience
        )


        demand_score = calculate_demand_score(
            career["demand"]
        )



        total_score = (

            skill_score
            +
            education_score
            +
            experience_score
            +
            demand_score

        )



        career_results.append({

            "career": career["name"],

            "category": career["category"],

            "match_score": total_score,


            "match_percentage": min(
                total_score,
                100
            ),


            "demand": career["demand"],


            "description":
            career["description"],


            "reasoning":
            generate_reason(
                profile,
                career
            ),


            "learning_path":
            career["learning_path"]

        })



    career_results.sort(

        key=lambda x: x["match_score"],

        reverse=True

    )



    recommendations = career_results[:3]



    return {


        "user": profile.name,


        "current_profile": {


            "education":
            profile.education,


            "experience":
            profile.experience,


            "skills":
            profile.skills,


            "goals":
            profile.goals

        },



        "career_recommendations":

        recommendations,



        "skill_gap": [

            "Advanced technical skills",

            "Industry certifications",

            "Real-world projects",

            "Cloud security",

            "Threat intelligence"

        ],



        "next_steps": [

            "Build cybersecurity portfolio projects",

            "Complete industry certifications",

            "Practice using enterprise security tools",

            "Develop professional network"

        ],



        "engine_version":

        "Decision Intelligence Engine v3"

    }