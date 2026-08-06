"""
Sentinel DNA Investigation Repository

Aggregates investigation data.
"""


from app.database.repository import Repository



class InvestigationRepository:


    def __init__(self):

        self.repository = Repository()



    def get_incident_context(
        self,
        incident_id,
    ):

        return {

            "incident":
                self.repository.get_incident(
                    incident_id
                ),

            "timeline":
                self.repository.get_timeline(
                    incident_id
                ),

        }