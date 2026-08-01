def recommend_certifications(target_career):

    certifications = {


        "AI Security Specialist": [

            "Security+",

            "AI Security Certification",

            "CySA+",

            "SC-200"

        ],


        "SOC Analyst": [

            "Security+",

            "CySA+",

            "SC-200"

        ],


        "Security Engineer": [

            "Security+",

            "CCNA Security",

            "CISSP"

        ]

    }


    return certifications.get(
        target_career,
        []
    )