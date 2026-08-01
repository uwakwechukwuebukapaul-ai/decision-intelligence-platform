"""
AI Career Planner Engine

Generates personalized cybersecurity
career execution plans.
"""


from app.data.careers import (
    get_career_profile
)



def generate_career_plan(
    career,
    user_skills=None
):


    if user_skills is None:

        user_skills = []



    career_profile = get_career_profile(
        career
    )



    if not career_profile:


        return {

            "error":
            "Career profile not found"

        }



    required_skills = (

        career_profile[
            "required_skills"
        ]

    )



    missing_skills = [

        skill

        for skill in required_skills

        if skill not in user_skills

    ]



    weeks = []




    week_number = 1



    for skill in missing_skills[:4]:


        weeks.append({


            "week":

            week_number,


            "focus":

            skill,



            "objectives":[


                f"Understand {skill} fundamentals",


                f"Practice {skill} using real SOC scenarios",


                f"Document {skill} knowledge"


            ],



            "recommended_actions":[


                f"Study {skill} concepts",


                f"Complete hands-on labs",


                f"Add {skill} evidence to portfolio"


            ]



        })



        week_number += 1





    return {


        "career":

        career,



        "level":

        career_profile[
            "level"
        ],



        "duration":

        f"{len(weeks)} weeks",



        "missing_skills":

        missing_skills,



        "recommended_tools":

        career_profile[
            "recommended_tools"
        ],



        "certifications":

        career_profile[
            "certifications"
        ],



        "weekly_plan":

        weeks



    }