from datetime import datetime



def generate_mentor_plan(profile, analysis):


    recommendations = analysis.get(
        "career_recommendations",
        []
    )


    if not recommendations:

        return {

            "status": "insufficient_data",

            "message":
            "No career recommendation available yet."

        }



    top_career = recommendations[0]


    target_role = top_career.get(
        "career",
        "Unknown"
    )


    missing_skills = top_career.get(
        "missing_skills",
        []
    )


    certifications = top_career.get(
        "certifications",
        []
    )



    return {


        "status": "success",


        "generated_at":

            datetime.now().strftime(
                "%Y-%m-%d"
            ),



        "student":

            profile.name,



        "target_role":

            target_role,



        "career_confidence":

            top_career.get(
                "confidence",
                "Unknown"
            ),



        "current_skills":

            profile.skills,



        "skill_priorities":

            missing_skills,



        "three_month_roadmap": [

            {

                "month": "Month 1",

                "focus":

                "Strengthen cybersecurity foundations",

                "tasks": [

                    "Improve Python automation skills",

                    "Practice Linux administration",

                    "Study networking fundamentals"

                ]

            },


            {

                "month": "Month 2",

                "focus":

                "Security operations skills",

                "tasks": [

                    "Learn SIEM concepts",

                    "Analyze security logs",

                    "Practice incident response"

                ]

            },


            {

                "month": "Month 3",

                "focus":

                "Build professional portfolio",

                "tasks": [

                    "Create cybersecurity projects",

                    "Document technical work",

                    "Publish portfolio"

                ]

            }

        ],



        "six_month_goal": [

            "Become internship/job ready",

            "Complete industry certifications",

            "Gain hands-on security experience"

        ],



        "recommended_projects": [

            {

                "project":

                "AI SOC Monitoring Dashboard",

                "purpose":

                "Practice threat detection and security analytics"

            },


            {

                "project":

                "Threat Intelligence Platform",

                "purpose":

                "Learn IOC enrichment and threat analysis"

            },


            {

                "project":

                "Vulnerability Scanner",

                "purpose":

                "Understand security assessment workflows"

            }

        ],



        "recommended_certifications":

            certifications if certifications else [

                "CompTIA Security+",

                "Certified SOC Analyst (CSA)",

                "Google Cybersecurity Certificate"

            ],



        "mentor_message": f"""

{profile.name}, your current strongest career direction is
{target_role}.

Your next priority should be closing your skill gaps,
building practical projects, and developing industry-ready
experience.

The roadmap above is designed to move you toward
professional readiness.

"""

    }