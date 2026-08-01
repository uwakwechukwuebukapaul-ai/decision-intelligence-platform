# ==========================================
# AI Mentor Engine v1
# Decision Intelligence Platform
# ==========================================


def generate_mentor_guidance(
    career,
    skills=None,
    progress=None,
    completed_labs=None,
    certifications=None
):


    # -------------------------------
    # Normalize Inputs
    # -------------------------------

    if skills is None:
        skills = []


    if progress is None:
        progress = 0


    if completed_labs is None:
        completed_labs = []


    if certifications is None:
        certifications = []



    if isinstance(skills, str):

        skills = [
            item.strip()
            for item in skills.split(",")
            if item.strip()
        ]



    # -------------------------------
    # Skill Intelligence
    # -------------------------------

    required_skills = [

        "SIEM",

        "Log Analysis",

        "Incident Response",

        "Threat Intelligence",

        "MITRE ATT&CK",

        "Detection Engineering"

    ]



    missing_skills = [

        skill

        for skill in required_skills

        if skill.lower()
        not in [
            s.lower()
            for s in skills
        ]

    ]



    strengths = [

        skill

        for skill in skills

        if skill.lower()
        not in [
            item.lower()
            for item in missing_skills
        ]

    ]



    # -------------------------------
    # Mentor Score
    # -------------------------------

    mentor_score = 0



    mentor_score += min(
        len(skills) * 10,
        40
    )


    mentor_score += min(
        progress,
        30
    )


    mentor_score += min(
        len(certifications) * 10,
        20
    )


    mentor_score += min(
        len(completed_labs) * 5,
        10
    )


    if mentor_score > 100:

        mentor_score = 100



    # -------------------------------
    # Daily Focus Generation
    # -------------------------------

    daily_focus = []


    for skill in missing_skills[:3]:

        daily_focus.append(

            f"Improve {skill} skills"

        )



    if not daily_focus:

        daily_focus = [

            "Practice advanced SOC investigations",

            "Build cybersecurity portfolio projects",

            "Improve threat detection capability"

        ]



    # -------------------------------
    # Mentor Message
    # -------------------------------

    if mentor_score < 40:


        message = (

            f"Your {career} journey has started. "

            "Focus on building strong cybersecurity foundations "

            "through practical labs and consistent learning."

        )


    elif mentor_score < 70:


        message = (

            f"You are making progress toward becoming a {career}. "

            "Continue improving missing technical skills "

            "and document your practical experience."

        )


    else:


        message = (

            f"You are developing strong readiness for a {career} role. "

            "Focus on advanced investigations, automation, "

            "and real-world SOC scenarios."

        )



    # -------------------------------
    # Return Intelligence Report
    # -------------------------------

    return {


        "career":

            career,


        "mentor_score":

            mentor_score,


        "mentor_message":

            message,


        "strengths":

            strengths,


        "skill_gaps":

            missing_skills,


        "daily_focus":

            daily_focus,


        "completed_labs":

            completed_labs,


        "certifications":

            certifications,


        "next_actions":

            [

                "Complete SOC investigation labs",

                "Practice SIEM detection engineering",

                "Map incidents to MITRE ATT&CK",

                "Build cybersecurity portfolio evidence"

            ]

    }