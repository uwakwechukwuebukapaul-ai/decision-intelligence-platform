from flask import Blueprint, request, jsonify

from app.database.db import SessionLocal
from app.models.user import UserProfile

from app.security.password import (
    hash_password,
    verify_password
)


auth_bp = Blueprint(
    "auth",
    __name__
)



@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.json


    db = SessionLocal()


    existing_user = db.query(
        UserProfile
    ).filter_by(
        email=data["email"]
    ).first()


    if existing_user:

        return jsonify(
            {
                "error":
                "Email already registered"
            }
        ), 400



    user = UserProfile(

        email=data["email"],

        password_hash=
        hash_password(
            data["password"]
        ),

        name=data["name"],

        education=data.get(
            "education"
        ),

        experience=data.get(
            "experience"
        ),

        skills=data.get(
            "skills"
        ),

        goals=data.get(
            "goals"
        ),

        constraints=data.get(
            "constraints"
        )

    )


    db.add(user)

    db.commit()

    db.close()


    return jsonify(
        {
            "message":
            "User registered successfully"
        }
    )



@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.json


    db = SessionLocal()


    user = db.query(
        UserProfile
    ).filter_by(
        email=data["email"]
    ).first()


    if not user:

        return jsonify(
            {
                "error":
                "Invalid credentials"
            }
        ),401



    if not verify_password(
        data["password"],
        user.password_hash
    ):

        return jsonify(
            {
                "error":
                "Invalid credentials"
            }
        ),401



    return jsonify(
        {
            "message":
            "Login successful",

            "user_id":
            user.id
        }
    )