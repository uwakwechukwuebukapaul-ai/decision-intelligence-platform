from flask import Blueprint, jsonify
import json

from app.database.db import SessionLocal

from app.models.user import UserProfile
from app.models.report import AIReport

from app.ai.decision_engine import analyze_profile

from app.ai.mentor.career_mentor import create_career_mentor

from app.ai.progress.progress_engine import generate_progress

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


    try:

        user = db.query(UserProfile).filter(
            UserProfile.id == user_id
        ).first()



        if not user:

            return jsonify({

                "error": "User not found"

            }), 404




        # ---------------------------------
        # AI Career Intelligence Analysis
        # ---------------------------------

        analysis = analyze_profile(
            user
        )




        recommendations = analysis.get(
            "career_recommendations",
            []
        )




        # ---------------------------------
        # AI Mentor Intelligence Engine
        # ---------------------------------

        if recommendations:


            top_career = recommendations[0]


            try:

                mentor = create_career_mentor(

                    user,

                    top_career

                )


                analysis["mentor"] = mentor


            except Exception as error:


                analysis["mentor"] = {

                    "error":
                    str(error)

                }




            # ---------------------------------
            # Career Readiness Intelligence
            # ---------------------------------

            try:

                readiness = generate_progress(

                    top_career["career"],

                    top_career.get(
                        "matched_skills",
                        []
                    )

                )


                analysis["readiness"] = readiness



            except Exception as error:


                analysis["readiness"] = {

                    "error":
                    str(error)

                }




        else:


            analysis["mentor"] = {}

            analysis["readiness"] = {}






        # ---------------------------------
        # Generate Final AI Report
        # ---------------------------------

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





        return jsonify({

            "message":
            "AI report generated and saved",


            "report_id":
            saved_report.id,


            "analysis":
            analysis

        })




    except Exception as error:


        db.rollback()


        return jsonify({

            "error":
            str(error)

        }), 500



    finally:


        db.close()