"""
AI Skill Gap Intelligence Engine

Responsible for:
- Comparing user skills against career requirements
- Detecting missing capabilities
- Prioritizing learning areas
- Generating recommendations

Future expansion:
- LLM reasoning
- Vector embeddings
- Industry skill graphs
- Real-time job market intelligence
"""


# =====================================================
# Career Knowledge Base
# =====================================================

CAREER_SKILLS = {

    "SOC Analyst": {

        "required_skills": [

            {
                "name": "SIEM",
                "priority": "High",
                "reason":
                "SOC analysts must monitor and investigate security events."
            },

            {
                "name": "Incident Response",
                "priority": "High",
                "reason":
                "Required for handling and documenting security incidents."
            },

            {
                "name": "Threat Hunting",
                "priority": "High",
                "reason":
                "Required to proactively discover threats."
            },

            {
                "name": "MITRE ATT&CK",
                "priority": "Medium",
                "reason":
                "Used for adversary behavior mapping and investigation."
            },

            {
                "name": "Networking",
                "priority": "Medium",
                "reason":
                "Required for understanding traffic and attacks."
            },

            {
                "name": "Python",
                "priority": "Medium",
                "reason":
                "Useful for automation and security scripting."
            }

        ]
    }

}



# =====================================================
# Normalize Skills
# =====================================================

def normalize_skills(skills):

    if not skills:

        return []


    if isinstance(skills, str):

        skills = skills.split(",")


    return [

        skill.strip().lower()

        for skill in skills

    ]





# =====================================================
# Skill Gap Analyzer
# =====================================================

def analyze_skill_gap(

    current_skills,

    target_career

):


    career = CAREER_SKILLS.get(

        target_career

    )


    if not career:


        return {

            "error":
            "Career profile not found"

        }



    user_skills = normalize_skills(

        current_skills

    )



    missing = []



    for skill in career["required_skills"]:


        if skill["name"].lower() not in user_skills:


            missing.append(skill)



    completed = [

        skill["name"]

        for skill in career["required_skills"]

        if skill["name"].lower() in user_skills

    ]



    recommendation = (

        missing[0]["name"]

        if missing

        else

        "Continue advanced training"

    )



    return {


        "career":

        target_career,


        "current_skills":

        completed,


        "skill_gap_count":

        len(missing),


        "missing_skills":

        missing,


        "recommended_next_skill":

        recommendation

    }