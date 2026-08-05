from datetime import datetime


class TimelineBuilder:
    """
    Investigation event timeline generator.
    """


    def build(self, events):

        timeline = []


        for index, event in enumerate(events):

            timeline.append({

                "sequence": index + 1,

                "timestamp":
                    datetime.utcnow().isoformat(),

                "event": event

            })


        return timeline