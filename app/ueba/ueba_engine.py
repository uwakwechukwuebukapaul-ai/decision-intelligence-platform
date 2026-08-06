from .behavior_repository import BehaviorRepository
from .behavior_schema import create_behavior_event
from .risk_model import BehaviorRiskModel



class UEBAEngine:


    def __init__(self):

        self.repository = BehaviorRepository()

        self.model = BehaviorRiskModel()



    def record_event(
        self,
        username,
        event_type,
        details
    ):

        event = create_behavior_event(
            username,
            event_type,
            details
        )


        return self.repository.save(
            event
        )



    def analyze_user(
        self,
        username
    ):

        events = self.repository.get_user_events(
            username
        )


        return {

            "username": username,

            "events": events,

            "risk":
                self.model.calculate(events)

        }