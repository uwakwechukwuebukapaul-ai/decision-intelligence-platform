from datetime import datetime
import uuid


class TimelineEngine:


    def __init__(self):

        self.events = []



    def add_event(
        self,
        case_id,
        event_type,
        description,
        source="AI_ENGINE"
    ):

        event = {

            "event_id": f"TIME-{uuid.uuid4().hex[:8].upper()}",

            "case_id": case_id,

            "event_type": event_type,

            "description": description,

            "source": source,

            "timestamp": datetime.utcnow().isoformat()

        }


        self.events.append(event)

        return event



    def get_timeline(
        self,
        case_id
    ):

        return [

            event
            for event in self.events
            if event["case_id"] == case_id

        ]



    def reconstruct_attack_chain(
        self,
        case_id
    ):

        timeline = self.get_timeline(
            case_id
        )

        return {

            "case_id": case_id,

            "attack_chain": timeline,

            "events_count": len(timeline),

            "status": "reconstructed"

        }