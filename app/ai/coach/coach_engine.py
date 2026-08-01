def generate_coach_plan(
    career,
    skills,
    progress,
    certifications
):

    missing_skills = [

        "SIEM",
        "Log Analysis",
        "Incident Response",
        "Threat Intelligence",
        "MITRE ATT&CK",
        "Detection Engineering"

    ]


    labs = [

        "Build Home SOC Lab",
        "Analyze Windows Event Logs",
        "Create SIEM Detection Rules",
        "Investigate Phishing Attacks",
        "Perform Threat Hunting"

    ]


    certifications_path = [

        "CompTIA Security+",
        "CompTIA CySA+",
        "Microsoft SC-200"

    ]



    if progress < 50:

        level = "Foundation Building"

    elif progress < 80:

        level = "SOC Analyst Preparation"

    else:

        level = "Job Ready"



    readiness = progress + len(skills) * 5


    if readiness > 100:

        readiness = 100



    return {


        "career":

        career,


        "stage":

        level,


        "readiness_score":

        readiness,


        "current_skills":

        skills,


        "skill_gaps":

        missing_skills,


        "recommended_labs":

        labs,


        "certification_path":

        certifications_path,


        "daily_focus":[

            "Practice SIEM investigations",

            "Analyze security logs",

            "Write detection rules",

            "Map threats to MITRE ATT&CK"

        ],


        "next_action":

        "Complete practical SOC investigation labs"


    }