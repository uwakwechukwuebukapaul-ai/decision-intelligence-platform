def generate_learning_plan(
    career,
    missing_skills,
    level="Beginner"
):


    roadmap = []


    week = 1



    for skill in missing_skills:


        roadmap.append({

            "week": week,

            "skill": skill,

            "objective":
            f"Master {skill} fundamentals",

            "tasks":[

                f"Study {skill}",

                f"Complete practical labs for {skill}",

                f"Build project related to {skill}"

            ],

            "status":
            "Not Started"

        })


        week += 1




    return {


        "engine":
        "AI Learning Roadmap Intelligence v1",


        "career":
        career,


        "level":
        level,


        "duration_weeks":
        len(roadmap),


        "roadmap":
        roadmap

    }