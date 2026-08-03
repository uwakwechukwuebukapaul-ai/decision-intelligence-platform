from datetime import datetime
import uuid
import json

from app.database.db import SessionLocal
from app.models.mission import Mission
from app.models.mission_result import MissionResult


class MissionManager:


    def __init__(self):

        pass



    def create_mission(
        self,
        title,
        objective,
        priority="medium"
    ):

        db = SessionLocal()

        try:

            mission = Mission(

                mission_id=
                    f"MISSION-{uuid.uuid4().hex[:8].upper()}",

                title=title,

                objective=objective,

                priority=priority,

                status="created"

            )


            db.add(mission)

            db.commit()

            db.refresh(mission)


            return self._serialize_mission(mission)


        finally:

            db.close()



    def list_missions(self):

        db = SessionLocal()

        try:

            missions = (
                db.query(Mission)
                .all()
            )


            return [

                self._serialize_mission(mission)

                for mission in missions

            ]


        finally:

            db.close()



    def get_mission(
        self,
        mission_id
    ):

        db = SessionLocal()

        try:

            return (

                db.query(Mission)

                .filter(
                    Mission.mission_id == mission_id
                )

                .first()

            )


        finally:

            db.close()



    def assign_mission(
        self,
        mission_id,
        agent_id
    ):

        db = SessionLocal()


        try:

            mission = (

                db.query(Mission)

                .filter(
                    Mission.mission_id == mission_id
                )

                .first()

            )


            if not mission:

                return None



            mission.assigned_agent = agent_id

            mission.status = "assigned"


            db.commit()

            db.refresh(mission)


            return self._serialize_mission(mission)


        finally:

            db.close()



    def complete_mission(
        self,
        mission_id,
        agent_id,
        result
    ):

        db = SessionLocal()


        try:

            mission = (

                db.query(Mission)

                .filter(
                    Mission.mission_id == mission_id
                )

                .first()

            )


            if not mission:

                return None



            mission.status = "completed"

            mission.completed_at = datetime.utcnow()



            mission_result = MissionResult(

                mission_id=mission_id,

                agent_id=agent_id,

                result=json.dumps(result)

            )


            db.add(
                mission_result
            )


            db.commit()


            return {

                "mission_id":
                    mission_id,

                "status":
                    "completed",

                "agent":
                    agent_id,

                "result":
                    result

            }


        finally:

            db.close()



    def _serialize_mission(
        self,
        mission
    ):

        return {

            "mission_id":
                mission.mission_id,

            "title":
                mission.title,

            "objective":
                mission.objective,

            "priority":
                mission.priority,

            "status":
                mission.status,

            "assigned_agent":
                mission.assigned_agent,

            "created_at":
                mission.created_at.isoformat()
                if mission.created_at else None,

            "completed_at":
                mission.completed_at.isoformat()
                if mission.completed_at else None

        }