from app.knowledge.career_database import CAREER_DATABASE


def normalize_skills(skills):

    if not skills:
        return []

    return [
        skill.strip().lower()
        for skill in skills.split(",")
        if skill.strip()
    ]



def calculate_match(user_skills, career):

    user_skill_list = normalize_skills(
        user_skills
    )


    required_skills = [
        skill.lower()
        for skill in career.get("skills", [])
    ]


    matched = []

    missing = []


    for skill in required_skills:

        if skill in user_skill_list:

            matched.append(skill)

        else:

            missing.append(skill)



    if required_skills:

        score = round(
            (len(matched) / len(required_skills)) * 100
        )

    else:

        score = 0



    return {

        "score": score,

        "matched_skills": matched,

        "missing_skills": missing

    }



def confidence_level(score):

    if score >= 80:

        return "High"

    elif score >= 50:

        return "Medium"

    else:

        return "Low"



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

            "confidence":
                confidence_level(
                    evaluation["score"]
                ),

            "description":
                career["description"],


            "matched_skills":
                evaluation["matched_skills"],


            "missing_skills":
                evaluation["missing_skills"],


            "certifications":
                career.get(
                    "certifications",
                    []
                )

        })



    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )



    recommendations = results[:3]



    if recommendations:


        top = recommendations[0]


        reasoning = f"""

{profile.name} is currently studying
{profile.education}.

Based on the current skills provided,
the strongest career direction is:

{top['career']}

Confidence Score:
{top['match_score']}%

Confidence Level:
{top['confidence']}

Why this recommendation:

Matched Skills:
{', '.join(top['matched_skills']) 
if top['matched_skills'] 
else 'No direct matches found'}

Priority Skills To Develop:

{', '.join(top['missing_skills'])
if top['missing_skills']
else 'Continue improving existing skills'}

Recommended Certifications:

{', '.join(top['certifications'])
if top['certifications']
else 'Industry certifications recommended'}

"""


        skill_gap = top["missing_skills"]

        certifications = top["certifications"]


    else:


        reasoning = """

No suitable career matches were found.

The system recommends adding more
technical skills to improve prediction accuracy.

"""


        skill_gap = []

        certifications = []



    return {


        "user": profile.name,


        "profile": {


            "education":
                profile.education,


            "experience":
                profile.experience,


            "skills":
                profile.skills


        },


        "career_recommendations":
            recommendations,


        "skill_gap":
            skill_gap,


        "certifications":
            certifications,


        "ai_reasoning":
            reasoning,


        "engine_version":

            "Decision Intelligence Engine v3.1"

    }