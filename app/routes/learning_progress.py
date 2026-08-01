from flask import Blueprint, jsonify

from datetime import datetime

from app.database.db import SessionLocal

from app.models.learning_progress import LearningProgress



learning_progress_bp = Blueprint(
    "learning_progress",
    __name__
)



@learning_progress_bp.route(
    "/learning/start/<int:user_id>/<int:week>",
    methods=["POST"]
)
def start_learning(user_id, week):

    db = SessionLocal()

    try:

        module = db.query(
            LearningProgress
        ).filter(

            LearningProgress.user_id == user_id,

            LearningProgress.week == week

        ).first()


        if not module:

            return jsonify({

                "error":
                "Learning module not found"

            }),404



        module.status = "Learning"

        module.progress = 10


        db.commit()


        return jsonify({

            "message":
            "Learning started",

            "week":
            week,

            "progress":
            module.progress

        })


    finally:

        db.close()





@learning_progress_bp.route(
    "/learning/complete/<int:user_id>/<int:week>",
    methods=["POST"]
)
def complete_learning(user_id, week):


    db = SessionLocal()


    try:

        module = db.query(
            LearningProgress
        ).filter(

            LearningProgress.user_id == user_id,

            LearningProgress.week == week

        ).first()



        if not module:

            return jsonify({

                "error":
                "Learning module not found"

            }),404



        module.status = "Completed"

        module.progress = 100

        module.completed_at = datetime.utcnow()


        db.commit()



        return jsonify({

            "message":
            "Module completed",

            "week":
            week,

            "progress":
            100

        })


    finally:

        db.close()