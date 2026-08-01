from datetime import datetime



def generate_report(profile, analysis):


    recommendations = analysis.get(
        "career_recommendations",
        []
    )


    mentor = analysis.get(
        "mentor",
        {}
    )



    report = {


        "title":
        "Career Decision Intelligence Report",



        "generated_at":
        datetime.now().strftime(
            "%Y-%m-%d"
        ),



        "engine": {

            "name":
            "Decision Intelligence Engine",

            "version":
            "v6",

            "type":
            "AI Career Mentor Intelligence System"

        },



        "user": {

            "name":
            profile.name,

            "education":
            profile.education,

            "experience":
            profile.experience,

            "skills":
            profile.skills,

            "goals":
            profile.goals

        },



        "recommendations":
        recommendations,



        "skill_gap":
        analysis.get(
            "skill_gap",
            []
        ),



        "ai_reasoning":
        analysis.get(
            "ai_reasoning",
            ""
        ),



        "confidence_score":
        analysis.get(
            "confidence_score",
            0
        ),



        "mentor": mentor


    }


    return report