def generate_roadmap(target_career):

    roadmaps = {

        "AI Security Specialist": {

            "duration": "6 Months",

            "months": [

                {
                    "month": "Month 1",
                    "focus": "AI Security Foundations",
                    "skills": [
                        "Advanced Python",
                        "Machine Learning Basics",
                        "Linux Security"
                    ],
                    "projects": [
                        "Build AI phishing detector",
                        "Create security automation scripts"
                    ]
                },


                {
                    "month": "Month 2",
                    "focus": "Machine Learning Security",
                    "skills": [
                        "Machine Learning",
                        "Adversarial Attacks",
                        "Model Security"
                    ],
                    "projects": [
                        "Build adversarial ML testing tool"
                    ]
                },


                {
                    "month": "Month 3",
                    "focus": "LLM Security",
                    "skills": [
                        "Prompt Injection",
                        "LLM Security",
                        "AI Governance"
                    ],
                    "projects": [
                        "Create LLM vulnerability scanner"
                    ]
                },


                {
                    "month": "Month 4",
                    "focus": "Security Engineering",
                    "skills": [
                        "Cloud Security",
                        "API Security",
                        "Automation"
                    ],
                    "projects": [
                        "Build AI SOC assistant"
                    ]
                },


                {
                    "month": "Month 5",
                    "focus": "Threat Intelligence",
                    "skills": [
                        "Threat Intelligence",
                        "Detection Engineering"
                    ],
                    "projects": [
                        "Create threat hunting project"
                    ]
                },


                {
                    "month": "Month 6",
                    "focus": "Career Launch",
                    "skills": [
                        "Security Research",
                        "Interview Preparation"
                    ],
                    "projects": [
                        "Publish cybersecurity portfolio",
                        "Build GitHub security projects"
                    ]
                }

            ]

        }

    }


    return roadmaps.get(
        target_career,
        {}
    )