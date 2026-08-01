"""
Cybersecurity Career Intelligence Database

Used by AI Decision Engine
"""



CAREERS = {


    "SOC Analyst": {


        "level":

        "Entry - Intermediate",



        "description":

        "Security Operations Center analyst responsible for monitoring, investigating and responding to security incidents.",



        "required_skills":[


            "SIEM",

            "Linux",

            "Python",

            "Log Analysis",

            "Incident Response",

            "Threat Intelligence",

            "MITRE ATT&CK"


        ],



        "recommended_tools":[


            "Splunk",

            "Microsoft Sentinel",

            "Wazuh",

            "Elastic Security"


        ],



        "certifications":[


            "CompTIA Security+",

            "CompTIA CySA+",

            "Microsoft SC-200"


        ]

    },





    "Threat Hunter": {


        "level":

        "Intermediate",



        "description":

        "Security professional who proactively searches environments for hidden threats.",



        "required_skills":[


            "Threat Hunting",

            "KQL",

            "Python",

            "MITRE ATT&CK",

            "Malware Analysis",

            "Digital Forensics"


        ],



        "recommended_tools":[


            "Microsoft Defender",

            "Velociraptor",

            "Splunk"


        ],



        "certifications":[


            "GIAC Threat Hunting",

            "CompTIA CySA+"


        ]

    },





    "Security Engineer": {


        "level":

        "Intermediate - Advanced",



        "description":

        "Engineer responsible for designing and maintaining security systems.",



        "required_skills":[


            "Network Security",

            "Cloud Security",

            "Firewalls",

            "Automation",

            "Python",

            "SIEM"


        ],



        "recommended_tools":[


            "Palo Alto",

            "Fortinet",

            "AWS Security",

            "Microsoft Sentinel"


        ],



        "certifications":[


            "Security+",

            "CISSP",

            "CCSP"


        ]

    }

}





def get_career_profile(career):


    return CAREERS.get(

        career,

        None

    )





def get_required_skills(career):


    profile = get_career_profile(career)


    if profile:


        return profile["required_skills"]


    return []