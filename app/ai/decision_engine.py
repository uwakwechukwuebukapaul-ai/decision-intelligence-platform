def analyze_profile(profile):
    """
    Basic Decision Intelligence engine.

    Takes a user profile and generates
    career recommendations.
    """

    recommendations = []

    skills = (profile.skills or "").lower()

    goals = (profile.goals or "").lower()


    # Skill-based reasoning

    if "python" in skills:
        recommendations.append(
            "AI Engineering or Automation roles"
        )


    if "security" in skills or "cyber" in skills:
        recommendations.append(
            "Cybersecurity and Security Engineering paths"
        )


    if "data" in skills:
        recommendations.append(
            "Data Analytics or Data Engineering paths"
        )


    # Default recommendation

    if not recommendations:
        recommendations.append(
            "Explore technology careers based on your interests and strengths"
        )


    report = {

        "user": profile.name,

        "current_profile": {
            "education": profile.education,
            "experience": profile.experience,
            "skills": profile.skills,
            "goals": profile.goals
        },

        "career_options": recommendations,


        "skill_gap": [
            "Advanced technical skills",
            "Real-world projects",
            "Professional portfolio"
        ],


        "next_steps": [
            "Build practical projects",
            "Develop industry skills",
            "Track progress regularly"
        ],


        "confidence": "Initial assessment"

    }


    return report