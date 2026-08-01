from datetime import datetime


def generate_report(profile, analysis):

    report = {

        "title": "Career Decision Intelligence Report",

        "generated_at": datetime.now().strftime(
            "%Y-%m-%d"
        ),


        "engine": {

            "name": "Decision Intelligence Engine",

            "version": "v2",

            "type": "AI Career Reasoning Engine"

        },


        "user": {

            "name": profile.name,

            "education": profile.education,

            "experience": profile.experience,

            "skills": profile.skills,

            "goals": profile.goals

        },


        "recommendations": analysis.get(
            "career_recommendations",
            []
        ),


        "skill_gap": analysis.get(
            "skill_gap",
            []
        ),


        "action_plan": analysis.get(
            "next_steps",
            []
        ),


        "confidence_score": calculate_confidence(
            analysis
        )

    }


    return report




def calculate_confidence(analysis):

    recommendations = analysis.get(
        "career_recommendations",
        []
    )


    if len(recommendations) >= 3:

        return 90


    elif len(recommendations) > 0:

        return 70


    return 40