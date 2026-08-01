from app.ai.analytics.analytics_database import CAREER_ANALYTICS



def calculate_career_intelligence(
    career,
    readiness_score,
    missing_skills
):


    market_data = CAREER_ANALYTICS.get(
        career,
        {}
    )


    market_demand = market_data.get(
        "market_demand",
        50
    )


    future_growth = market_data.get(
        "future_growth",
        50
    )


    industry_score = market_data.get(
        "industry_score",
        50
    )



    skill_readiness = readiness_score



    overall_score = round(

        (

            skill_readiness +

            market_demand +

            future_growth +

            industry_score

        ) / 4

    )



    return {


        "career":
        career,


        "skill_readiness":
        skill_readiness,


        "market_demand":
        market_demand,


        "future_growth":
        future_growth,


        "industry_score":
        industry_score,


        "overall_intelligence_score":
        overall_score,


        "priority_skills":
        missing_skills


    }