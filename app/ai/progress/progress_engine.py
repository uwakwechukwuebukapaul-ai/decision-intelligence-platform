from app.ai.progress.evolution_engine import evaluate_growth


def generate_progress(
    career,
    completed_skills
):


    career_skills = {


        "AI Security Specialist":

        [
            "python",
            "security",
            "machine learning",
            "automation",
            "cloud security"
        ],



        "SOC Analyst":

        [
            "linux",
            "siem",
            "incident response",
            "network security"
        ],



        "Security Engineer":

        [
            "network security",
            "linux",
            "firewalls",
            "cloud security"
        ]


    }



    required = career_skills.get(
        career,
        []
    )


    completed = []


    missing = []



    for skill in required:


        if skill in completed_skills:


            completed.append(skill)


        else:


            missing.append(skill)




    if required:


        readiness = round(
            (len(completed) /
            len(required)) * 100
        )


    else:


        readiness = 0




    growth = evaluate_growth(
        readiness
    )



    return {


        "career": career,


        "readiness_score":
            readiness,


        "completed_skills":
            completed,


        "missing_skills":
            missing,


        "career_level":
            growth["career_level"],


        "recommendation":
            growth["recommendation"]


    }