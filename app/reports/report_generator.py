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


    readiness = analysis.get(
        "readiness",
        {}
    )


    evolution = analysis.get(
        "evolution",
        {}
    )


    learning_plan = analysis.get(
        "learning_plan",
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
            "v12",

            "type":
            "AI Career Intelligence Platform"

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



        "certifications":
        analysis.get(
            "certifications",
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



        # AI Mentor Intelligence

        "mentor":
        mentor,



        # Career Readiness Intelligence

        "readiness":
        readiness,



        # Career Growth Evolution Intelligence

        "evolution":
        evolution,



        # AI Learning Recommendation Engine

        "learning_plan":
        learning_plan


    }


    return report