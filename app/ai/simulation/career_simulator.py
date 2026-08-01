def simulate_career_growth(
    career,
    skills,
    progress,
    certifications,
    labs
):


    base_score = progress



    missing_skills = [

        "SIEM",

        "Log Analysis",

        "Incident Response",

        "Threat Intelligence",

        "MITRE ATT&CK",

        "Detection Engineering"

    ]



    completed_skills = [

        skill

        for skill in missing_skills

        if skill not in skills

    ]



    six_month_score = min(
        base_score + 20,
        100
    )


    twelve_month_score = min(
        base_score + 35,
        100
    )



    return {


        "career_target":

            career,



        "current_profile":{


            "skills":

                skills,


            "certifications":

                certifications,


            "labs":

                labs,


            "readiness":

                base_score

        },



        "simulation":{


            "6_months":{


                "estimated_readiness":

                    six_month_score,


                "focus":[

                    "Improve SIEM skills",

                    "Practice incident investigations",

                    "Build detection rules"

                ]

            },



            "12_months":{


                "estimated_readiness":

                    twelve_month_score,


                "focus":[

                    "Threat Hunting",

                    "MITRE ATT&CK Mapping",

                    "Detection Engineering"

                ]

            }

        },



        "prediction":{


            "status":

            "Positive Growth Path",



            "message":

            f"You are progressing toward becoming a {career}"

        }

    }