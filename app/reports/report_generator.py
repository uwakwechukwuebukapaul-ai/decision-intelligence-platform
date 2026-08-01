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


    simulation = analysis.get(
        "simulation",
        {}
    )


    learning = analysis.get(
        "learning",
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
            "v15",

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



        # Career Evolution Intelligence

        "evolution":
        evolution,



        # Career Simulation Intelligence

        "simulation":
        simulation,



        # Learning Intelligence v15

        "learning":
        learning


    }


    return report