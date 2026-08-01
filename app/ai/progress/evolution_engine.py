def evaluate_growth(
    readiness_score
):


    if readiness_score >= 80:


        level = "Advanced"


        recommendation = (
            "Ready for professional opportunities"
        )


    elif readiness_score >= 50:


        level = "Intermediate"


        recommendation = (
            "Continue building projects and certifications"
        )


    else:


        level = "Beginner"


        recommendation = (
            "Focus on foundational skills"
        )



    return {


        "career_level": level,


        "recommendation":
            recommendation


    }