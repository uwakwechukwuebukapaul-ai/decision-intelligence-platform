from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.ai.decision_engine import analyze_profile

from app.ai.mentor.career_mentor import generate_mentor_plan

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



    user = db.query(
        UserProfile
    ).filter(
        UserProfile.id == user_id
    ).first()



    if not user:


        db.close()


        return jsonify({

            "error":
            "User not found"

        }),404




    analysis = analyze_profile(
        user
    )



    mentor_plan = generate_mentor_plan(

        user,

        analysis

    )



    analysis["mentor_plan"] = mentor_plan




    report = generate_report(

        user,

        analysis

    )



    db.close()




    return jsonify({

        "message":

        "AI report generated and saved",


        "analysis":

        analysis,


        "mentor_plan":

        mentor_plan,


        "report":

        report

    })