def generate_certification_path(career):


    certification_database = {


        "SOC Analyst": [

            {
                "name": "CompTIA Security+",
                "priority": "High",
                "timeline": "1-2 Months",
                "reason":
                "Build cybersecurity fundamentals, networking and security concepts"
            },


            {
                "name": "Microsoft SC-200",
                "priority": "High",
                "timeline": "2-3 Months",
                "reason":
                "Learn security operations and Microsoft Sentinel"
            },


            {
                "name": "CompTIA CySA+",
                "priority": "Medium",
                "timeline": "3-6 Months",
                "reason":
                "Develop threat detection and incident response skills"
            }

        ],



        "Security Engineer": [

            {
                "name":"CompTIA Security+",
                "priority":"High",
                "timeline":"1-2 Months",
                "reason":
                "Security foundation"
            },


            {
                "name":"Cisco CCNA",
                "priority":"Medium",
                "timeline":"3 Months",
                "reason":
                "Networking and infrastructure security"
            }

        ],



        "AI Security Specialist":[


            {
                "name":"Security+",
                "priority":"High",
                "timeline":"2 Months",
                "reason":
                "Cybersecurity foundation"
            },


            {
                "name":"AI Engineering Certification",
                "priority":"Medium",
                "timeline":"6 Months",
                "reason":
                "Artificial intelligence systems knowledge"
            }

        ]

    }



    certifications = certification_database.get(

        career,

        []

    )



    return {


        "career": career,


        "certifications": certifications,


        "total_certifications":

        len(certifications)

    }