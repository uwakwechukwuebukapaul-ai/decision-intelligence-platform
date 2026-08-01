from app.ai.mentor.roadmap_engine import generate_roadmap
from app.ai.mentor.certification_engine import recommend_certifications
from app.ai.mentor.project_generator import generate_projects



def calculate_readiness(profile, career):

    completed = []

    missing = []


    skills = [
        skill.strip().lower()
        for skill in profile.skills.split(",")
    ]


    requirements = {

        "AI Security Specialist": [

            "python",
            "security",
            "machine learning",
            "automation",
            "cloud security"

        ],


        "SOC Analyst": [

            "security",
            "linux",
            "siem",
            "incident response"

        ]

    }


    required = requirements.get(
        career,
        []
    )


    for skill in required:

        if skill in skills:

            completed.append(skill)

        else:

            missing.append(skill)



    if not required:

        score = 0

    else:

        score = round(
            (len(completed) / len(required)) * 100
        )


    return {

        "score": score,

        "completed_skills": completed,

        "missing_skills": missing

    }



def create_career_mentor(profile, recommendation):


    target = recommendation.get(
        "career",
        ""
    )


    readiness = calculate_readiness(
        profile,
        target
    )


    return {


        "target_career":
        target,


        "readiness_score":
        readiness["score"],


        "completed_skills":
        readiness["completed_skills"],


        "missing_skills":
        readiness["missing_skills"],


        "roadmap":
        generate_roadmap(
            target
        ),


        "certifications":
        recommend_certifications(
            target
        ),


        "projects":
        generate_projects(
            target
        )

    }