from flask import Blueprint, jsonify

from app.database.db import SessionLocal
from app.models.user import UserProfile

from app.ai.decision_engine import analyze_profile


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
            "error": "User not found"
        }), 404


    report = analyze_profile(user)


    db.close()


    return jsonify(report)