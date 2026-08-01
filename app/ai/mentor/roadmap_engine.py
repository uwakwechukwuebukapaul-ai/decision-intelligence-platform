from app.knowledge.roadmap_database import ROADMAP_DATABASE



def generate_roadmap(career):


    roadmap = ROADMAP_DATABASE.get(
        career,
        {}
    )


    return {


        "target_career": career,


        "duration": roadmap.get(
            "duration",
            "Unknown"
        ),


        "roadmap": roadmap.get(
            "months",
            []
        )


    }