from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.models.learning_progress import LearningProgress



decision_bp = Blueprint(
    "decision",
    __name__
)



@decision_bp.route(
    "/decision/<int:user_id>",
    methods=["GET"]
)
def decision_engine(user_id):

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
                module
                for module in modules
                if module.status == "Completed"
            ]
        )



        total = len(modules)



        if total > 0:

            progress_score = int(
                (completed / total) * 100
            )

        else:

            progress_score = 0




        readiness_score = min(

            40 +

            progress_score,

            100

        )



        return jsonify({

            "user":

            user.name,



            "career":

            "SOC Analyst",



            "readiness_score":

            readiness_score,



            "analysis":{


                "strengths":[

                    user.skills

                ],


                "gaps":[

                    "SIEM",

                    "Incident Response",

                    "Threat Hunting"

                ]

            },



            "decision":{


                "priority":

                "Build SIEM investigation skills first",



                "next_actions":[

                    "Complete SIEM fundamentals",

                    "Practice log analysis",

                    "Create detection rules"

                ]

            }

        })



    finally:

        db.close()