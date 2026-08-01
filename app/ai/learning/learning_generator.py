from app.database.db import SessionLocal

from app.models.learning_progress import LearningProgress



def generate_learning_plan(
    user_id,
    career,
    missing_skills
):

    db = SessionLocal()


    try:

        roadmap = []

        week = 1


        for skill in missing_skills:


            # Check if module already exists
            existing_module = db.query(
                LearningProgress
            ).filter(

                LearningProgress.user_id == user_id,

                LearningProgress.week == week

            ).first()



            if existing_module:

                module = existing_module


            else:


                module = LearningProgress(

                    user_id=user_id,

                    week=week,

                    skill_name=skill,

                    objective=f"Master {skill} fundamentals",

                    status="Not Started",

                    progress=0,

                    notes=f"Career track: {career}"

                )


                db.add(module)



            roadmap.append({

                "id": module.id,

                "week": week,

                "skill": skill,

                "objective":
                f"Master {skill} fundamentals",

                "status":
                module.status,

                "progress":
                module.progress

            })


            week += 1



        db.commit()



        return {


            "engine":
            "AI Learning Roadmap Generator v2",


            "career":
            career,


            "modules_created":
            len(roadmap),


            "roadmap":
            roadmap

        }




    except Exception as error:


        db.rollback()


        return {


            "error":
            str(error)

        }




    finally:


        db.close()