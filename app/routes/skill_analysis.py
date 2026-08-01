from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.ai.skill_analysis.skill_gap_engine import analyze_skill_gap



skill_analysis_bp = Blueprint(
    "skill_analysis",
    __name__
)



@skill_analysis_bp.route(
    "/analysis/skill-gap/<int:user_id>",
    methods=["GET"]
)
def skill_gap_analysis(user_id):


    db = SessionLocal()


    try:


        user = db.query(
            UserProfile
        ).filter(

            UserProfile.id == user_id

        ).first()



        if not user:

            return jsonify({

                "error":
                "User not found"

            }),404




        target_career = "SOC Analyst"



        result = analyze_skill_gap(

            user.skills,

            target_career

        )



        return jsonify({

            "user":

            user.name,


            "user_id":

            user.id,


            "analysis":

            result

        })



    except Exception as error:


        return jsonify({

            "error":

            str(error)

        }),500



    finally:

        db.close()