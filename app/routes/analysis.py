from flask import Blueprint, jsonify
import json

from app.database.db import SessionLocal

from app.models.user import UserProfile
from app.models.report import AIReport

from app.ai.decision_engine import analyze_profile

from app.ai.mentor.career_mentor import create_career_mentor

from app.reports.report_generator import generate_report



analysis_bp = Blueprint(
    "analysis",
    __name__
)



@analysis_bp.route(
    "/analysis/<int:user_id>",
    methods=["GET"]
)
def create_analysis(user_id):


    db = SessionLocal()



    user = db.query(UserProfile).filter(
        UserProfile.id == user_id
    ).first()



    if not user:


        db.close()


        return jsonify({

            "error":
            "User not found"

        }), 404




    # Generate AI career analysis

    analysis = analyze_profile(
        user
    )




    # Generate AI Mentor roadmap

    recommendations = analysis.get(
        "career_recommendations",
        []
    )


    if recommendations:


        mentor = create_career_mentor(

            user,

            recommendations[0]

        )


        analysis["mentor"] = mentor



    else:


        analysis["mentor"] = {}





    # Generate final intelligence report

    report = generate_report(

        user,

        analysis

    )





    saved_report = AIReport(

        user_id=user.id,

        report_content=json.dumps(
            report
        )

    )




    db.add(saved_report)


    db.commit()


    db.refresh(
        saved_report
    )



    db.close()




    return jsonify({

        "message":
        "AI report generated and saved",


        "report_id":
        saved_report.id,


        "analysis":
        analysis

    })