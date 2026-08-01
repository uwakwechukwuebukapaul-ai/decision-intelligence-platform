from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.models.learning_progress import LearningProgress

from app.ai.learning.learning_generator import generate_learning_plan



learning_bp = Blueprint(
    "learning",
    __name__
)





# =====================================================
# AI Learning Roadmap Endpoint
# =====================================================


@learning_bp.route(
    "/learning-plan/<int:user_id>",
    methods=["GET"]
)
def learning_plan(user_id):


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




        roadmap = [

            {

                "week":1,

                "skill":
                "SIEM",

                "objective":
                "Master SIEM fundamentals",

                "status":
                "Not Started",

                "tasks":[

                    "Learn SIEM architecture",

                    "Study log collection",

                    "Create detection rules"

                ]

            },


            {

                "week":2,

                "skill":
                "Incident Response",

                "objective":
                "Master incident response fundamentals",

                "status":
                "Not Started",

                "tasks":[

                    "Study incident lifecycle",

                    "Investigate security alerts",

                    "Write incident reports"

                ]

            },


            {

                "week":3,

                "skill":
                "Threat Hunting",

                "objective":
                "Master threat hunting fundamentals",

                "status":
                "Not Started",

                "tasks":[

                    "Learn IOC investigation",

                    "Practice hypothesis hunting",

                    "Map threats to MITRE ATT&CK"

                ]

            }

        ]



        return jsonify({

            "engine":

            "AI Learning Roadmap Intelligence v2",


            "user":

            user.name,


            "career":

            "SOC Analyst",


            "level":

            "Beginner",


            "duration_weeks":

            len(roadmap),


            "roadmap":

            roadmap

        })



    finally:

        db.close()







# =====================================================
# AI Learning Generator
# =====================================================


@learning_bp.route(
    "/learning/generate/<int:user_id>",
    methods=["POST"]
)
def generate_plan(user_id):


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





        missing_skills = [

            "SIEM",

            "Incident Response",

            "Threat Hunting"

        ]




        result = generate_learning_plan(

            user_id,

            "SOC Analyst",

            missing_skills

        )




        return jsonify(result)




    except Exception as error:


        return jsonify({

            "error":

            str(error)

        }),500




    finally:

        db.close()







# =====================================================
# Learning Progress View
# =====================================================


@learning_bp.route(
    "/learning/progress/<int:user_id>",
    methods=["GET"]
)
def learning_progress(user_id):


    db = SessionLocal()


    try:


        modules = db.query(

            LearningProgress

        ).filter(

            LearningProgress.user_id == user_id

        ).all()




        return jsonify({

            "user_id":

            user_id,


            "modules":


            [

                {


                    "skill":

                    module.skill_name,


                    "status":

                    module.status,


                    "progress":

                    module.progress,


                    "notes":

                    module.notes

                }


                for module in modules

            ]

        })




    finally:


        db.close()