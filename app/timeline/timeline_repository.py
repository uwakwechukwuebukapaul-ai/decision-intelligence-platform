"""
Sentinel DNA Timeline Repository
"""


from app.database.repository import Repository



class TimelineRepository:


    def __init__(self):

        self.repository = Repository()



    def save(
        self,
        event
    ):

        return self.repository.save_timeline_event(
            event
        )



    def get(
        self,
        incident_id
    ):

        return self.repository.get_timeline(
            incident_id
        )