# ==================================
# AI Career Advisor Engine
# ==================================


def generate_career_advice(
        career,
        skills
):


    if isinstance(skills, str):

        skills = [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]



    advice = {


        "career":

            career,



        "current_skills":

            skills,



        "recommendations":

            [


                "Improve SIEM investigation skills",


                "Practice Windows and Linux log analysis",


                "Build incident response experience",


                "Learn MITRE ATT&CK mapping",


                "Create SOC portfolio projects"


            ],



        "next_steps":

            [


                "Complete SIEM labs",


                "Analyze real security events",


                "Create detection rules",


                "Document investigations"



            ]

    }


    return advice