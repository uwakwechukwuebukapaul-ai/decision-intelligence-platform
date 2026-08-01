def build_user_intelligence(
    user,
    skills=None,
    progress=None,
    certifications=None,
    labs=None
):

    intelligence = {


        "user": {

            "id": user.id,

            "name": user.name

        },


        "career": {


            "target":

                getattr(
                    user,
                    "goal",
                    "Cybersecurity Professional"
                )

        },


        "skills": {


            "completed":

                skills or [],


            "skill_count":

                len(skills or [])

        },


        "learning": {


            "progress":

                progress or 0

        },


        "certifications": certifications or [],



        "labs": labs or []

    }



    # Intelligence scoring

    score = 0


    score += len(skills or []) * 5

    score += int(progress or 0)



    if certifications:

        score += len(certifications) * 10



    intelligence["readiness"] = {


        "score":

            min(score,100),


        "level":

            calculate_level(score)

    }



    intelligence["recommendations"] = {


        "next_focus":

            generate_focus(skills or [])


    }



    return intelligence




def calculate_level(score):

    if score < 40:

        return "Beginner"


    elif score < 70:

        return "Developing"


    else:

        return "Advanced"




def generate_focus(skills):


    required = [

        "SIEM",

        "Incident Response",

        "Threat Hunting",

        "Detection Engineering",

        "MITRE ATT&CK"

    ]


    missing = [

        skill

        for skill in required

        if skill not in skills

    ]


    return missing[:3]