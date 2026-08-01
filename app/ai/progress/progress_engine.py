from app.ai.progress.readiness_engine import (
    readiness_report
)



def generate_progress(
    career,
    completed_skills
):


    required_skills = [

        "python",

        "security",

        "linux",

        "machine learning",

        "cloud security",

        "automation"

    ]


    return readiness_report(

        career,

        completed_skills,

        required_skills

    )