from flask import Blueprint, request, jsonify

from app.database.db import SessionLocal
from app.models.user import UserProfile


profile_bp = Blueprint(
    "profile",
    __name__
)


@profile_bp.route("/profile", methods=["POST"])
def create_profile():

    data = request.json

    db = SessionLocal()

    user = UserProfile(
        name=data.get("name"),
        education=data.get("education"),
        experience=data.get("experience"),
        skills=data.get("skills"),
        goals=data.get("goals"),
        constraints=data.get("constraints")
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()

    return jsonify({
        "message": "Profile created",
        "id": user.id
    })