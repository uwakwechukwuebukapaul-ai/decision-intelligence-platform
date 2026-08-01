def generate_projects(target_career):

    projects = {


        "AI Security Specialist": [

            {
                "name":
                "AI Phishing Detection Platform",

                "skills":
                [
                    "Python",
                    "Machine Learning",
                    "Threat Intelligence"
                ],

                "difficulty":
                "Intermediate"

            },


            {
                "name":
                "LLM Security Scanner",

                "skills":
                [
                    "Python",
                    "AI Security",
                    "Prompt Injection Testing"
                ],

                "difficulty":
                "Advanced"

            }

        ]

    }


    return projects.get(
        target_career,
        []
    )