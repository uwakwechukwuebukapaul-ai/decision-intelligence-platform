from datetime import datetime


def generate_report(profile, analysis):

    report = {

        "title": "Career Decision Intelligence Report",

        "generated_at": datetime.now().strftime(
            "%Y-%m-%d"
        ),

        "user": {

            "name": profile.name,

            "education": profile.education,

            "experience": profile.experience,

            "skills": profile.skills

        },


        "recommendations": analysis.get(
            "career_options",
            []
        ),


        "skill_gap": analysis.get(
            "skill_gap",
            []
        ),


        "action_plan": analysis.get(
            "next_steps",
            []
        )

    }


    return report