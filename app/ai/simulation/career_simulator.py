from app.ai.simulation.simulation_database import SIMULATION_DATA



def simulate_career_growth(
    career,
    readiness_score,
    missing_skills
):


    timeline = []


    for stage in SIMULATION_DATA:


        improvement = stage["increase"]


        projected_score = min(
            readiness_score + improvement,
            100
        )


        timeline.append({

            "period":
            stage["period"],


            "projected_readiness":
            projected_score,


            "focus":
            stage["focus"],


            "expected_outcome":
            stage["outcome"]

        })



    return {


        "career":
        career,


        "starting_readiness":
        readiness_score,


        "missing_skills":
        missing_skills,


        "simulation":
        timeline,


        "engine":
        "Career Simulation Engine v1"

    }