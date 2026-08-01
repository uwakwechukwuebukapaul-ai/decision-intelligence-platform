from app.models.skill_progress import SkillProgress


def generate_skill_progress(
    db,
    user_id,
    missing_skills
):

    created_skills = []


    for skill in missing_skills:


        existing = (
            db.query(SkillProgress)
            .filter(
                SkillProgress.user_id == user_id,
                SkillProgress.skill_name == skill
            )
            .first()
        )


        if existing:
            continue



        new_skill = SkillProgress(

            user_id=user_id,

            skill_name=skill,

            level="Beginner",

            progress=0,

            status="Not Started"

        )


        db.add(new_skill)


        created_skills.append(skill)



    db.commit()


    return created_skills