def run_ai_orchestrator(
    user_intelligence,
    advisor,
    mentor,
    coach,
    recommendation,
    decision,
    career_report
):


    return {


        "platform":

        "Decision Intelligence Platform",



        "user":

        user_intelligence.get(
            "user"
        ),



        "career":

        user_intelligence.get(
            "career"
        ),



        "readiness":

        user_intelligence.get(
            "readiness"
        ),



        "ai_modules":{


            "advisor":

            advisor,


            "mentor":

            mentor,


            "coach":

            coach,


            "recommendation":

            recommendation,


            "decision":

            decision,


            "career_report":

            career_report

        },



        "next_priority":

        determine_priority(
            user_intelligence
        )

    }





def determine_priority(
    intelligence
):


    focus = (

        intelligence
        .get(
            "recommendations",
            {}
        )
        .get(
            "next_focus",
            []
        )

    )


    if focus:

        return focus[0]


    return "Continue skill development"