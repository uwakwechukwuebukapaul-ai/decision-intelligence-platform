from datetime import datetime


def generate_report(profile, analysis):

    report = {

        "title": "Career Decision Intelligence Report",

        "generated_at": datetime.now().strftime(
            "%Y-%m-%d"
        ),


        "engine": {

            "name": "Decision Intelligence Engine",

            "version": "v5",

            "type": "AI Career Intelligence System"

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


        "ai_reasoning": analysis.get(
            "ai_reasoning",
            ""
        ),


        "roadmap": analysis.get(
            "roadmap",
            {}
        ),


        "confidence_score": analysis.get(
            "confidence_score",
            90
        )

    }


    return report