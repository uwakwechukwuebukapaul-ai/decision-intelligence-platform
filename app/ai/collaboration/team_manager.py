from datetime import datetime
import uuid
import json

from app.database.db import SessionLocal
from app.models.team import Team



class TeamManager:


    def __init__(self):

        self.db = SessionLocal()



    def create_team(
        self,
        name,
        mission_id,
        agents
    ):


        team = Team(

            team_id=
                f"TEAM-{uuid.uuid4().hex[:8].upper()}",

            name=
                name,

            mission_id=
                mission_id,

            agents=
                json.dumps(agents),

            status=
                "active"

        )


        self.db.add(team)

        self.db.commit()

        self.db.refresh(team)



        return self.serialize(team)




    def list_teams(self):


        teams = self.db.query(
            Team
        ).all()



        return {

            "team_count":
                len(teams),

            "teams":
                [
                    self.serialize(team)
                    for team in teams
                ]

        }




    def get_team(
        self,
        team_id
    ):


        team = self.db.query(
            Team
        ).filter(
            Team.team_id == team_id
        ).first()



        if not team:

            return None



        return self.serialize(team)




    def serialize(
        self,
        team
    ):


        return {

            "team_id":
                team.team_id,

            "name":
                team.name,

            "mission_id":
                team.mission_id,

            "agents":
                json.loads(team.agents),

            "status":
                team.status,

            "created_at":
                team.created_at.isoformat()

        }