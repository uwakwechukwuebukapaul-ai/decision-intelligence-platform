from flask import Blueprint, request, jsonify

from datetime import datetime

from app.database.db import SessionLocal

from app.models.skill_progress import SkillProgress
from app.models.user import UserProfile



skills_bp = Blueprint(
    "skills",
    __name__
)



# =====================================
# Add New Skill Progress
# =====================================

@skills_bp.route(
    "/skills/add",
    methods=["POST"]
)
def add_skill():


    db = SessionLocal()


    try:

        data = request.json


        user_id = data.get(
            "user_id"
        )

        skill_name = data.get(
            "skill_name"
        )


        if not user_id or not skill_name:

            return jsonify({

                "error":
                "user_id and skill_name required"

            }), 400



        user = db.query(UserProfile).filter(
            UserProfile.id == user_id
        ).first()



        if not user:

            return jsonify({

                "error":
                "User not found"

            }),404




        skill = SkillProgress(

            user_id=user_id,

            skill_name=skill_name,

            level=data.get(
                "level",
                "Beginner"
            ),

            progress=data.get(
                "progress",
                0
            )

        )


        db.add(skill)

        db.commit()

        db.refresh(skill)



        return jsonify({

            "message":
            "Skill progress added",

            "skill_id":
            skill.id

        })



    finally:

        db.close()






# =====================================
# Get User Skills
# =====================================


@skills_bp.route(
    "/skills/user/<int:user_id>",
    methods=["GET"]
)
def get_user_skills(user_id):


    db = SessionLocal()


    try:


        skills = db.query(
            SkillProgress
        ).filter(

            SkillProgress.user_id == user_id

        ).all()



        result = []


        for skill in skills:


            result.append({

                "id":
                skill.id,

                "skill":
                skill.skill_name,

                "level":
                skill.level,

                "progress":
                skill.progress,

                "status":
                skill.status

            })



        return jsonify(result)



    finally:

        db.close()







# =====================================
# Update Skill Progress
# =====================================


@skills_bp.route(
    "/skills/update/<int:skill_id>",
    methods=["PUT"]
)
def update_skill(skill_id):


    db = SessionLocal()


    try:


        skill = db.query(
            SkillProgress
        ).filter(

            SkillProgress.id == skill_id

        ).first()



        if not skill:


            return jsonify({

                "error":
                "Skill not found"

            }),404




        data = request.json



        if "progress" in data:

            skill.progress = data["progress"]



        if "level" in data:

            skill.level = data["level"]





        if skill.progress >= 100:


            skill.status = "Completed"

            skill.completed_at = datetime.utcnow()



        else:

            skill.status = "Learning"




        db.commit()



        return jsonify({

            "message":
            "Skill updated successfully"

        })



    finally:

        db.close()