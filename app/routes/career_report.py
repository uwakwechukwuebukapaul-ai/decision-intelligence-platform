from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.models.learning_progress import LearningProgress


career_report_bp = Blueprint(
    "career_report",
    __name__
)



@career_report_bp.route(
    "/career-report/<int:user_id>",
    methods=["GET"]
)
def career_report(user_id):

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



        modules = db.query(
            LearningProgress
        ).filter(
            LearningProgress.user_id == user_id
        ).all()



        completed = len(
            [
                m for m in modules
                if m.status == "Completed"
            ]
        )


        return jsonify({

            "user":
            user.name,


            "career_target":
            "SOC Analyst",


            "profile":{

                "education":
                user.education,


                "experience":
                user.experience

            },


            "skills":
            user.skills,


            "learning_status":{

                "completed":
                completed,


                "total_modules":
                len(modules),


                "remaining":
                len(modules)-completed

            },


            "recommendation":
            "Continue SOC training path focusing on SIEM, Incident Response and Threat Hunting."

        })


    finally:

        db.close()