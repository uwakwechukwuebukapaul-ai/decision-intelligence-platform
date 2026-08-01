"""
AI Recommendation Engine

Generates personalized cybersecurity career recommendations.
"""


def generate_recommendations(
    career,
    missing_skills
):

    recommendations = {

        "skills": missing_skills,


        "labs": [

            "Build a Home SOC Lab",

            "Analyze Windows Event Logs",

            "Create SIEM Detection Rules",

            "Investigate Malware Indicators",

            "Perform Threat Hunting Exercises"

        ],


        "projects": [

            "AI Phishing Email Detector",

            "SOC Investigation Dashboard",

            "Threat Intelligence Platform",

            "Incident Response Automation Tool"

        ],


        "certifications": [

            "CompTIA Security+",

            "CompTIA CySA+",

            "Microsoft SC-200",

            "Splunk Core Certified User"

        ],


        "tools_to_learn": [

            "Microsoft Sentinel",

            "Splunk",

            "Wazuh",

            "Elastic Security",

            "Wireshark",

            "MITRE ATT&CK"

        ]

    }


    return {


        "career": career,


        "recommendations": recommendations


    }