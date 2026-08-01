from app.ai.learning.learning_database import LEARNING_DATABASE



def generate_learning_plan(
    missing_skills
):


    recommendations = []



    for skill in missing_skills:


        data = LEARNING_DATABASE.get(
            skill.lower()
        )


        if data:


            recommendations.append({

                "skill": skill,

                "courses":
                    data["courses"],

                "certifications":
                    data["certifications"],

                "projects":
                    data["projects"]

            })



    return {


        "learning_plan":
            recommendations,


        "engine_version":
        "Learning Intelligence Engine v1"

    }