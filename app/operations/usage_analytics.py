from datetime import datetime



class UsageAnalytics:



    def __init__(self):

        self.events = []



    def track(

        self,

        user,

        action

    ):


        event = {


            "user":

                user,


            "action":

                action,


            "timestamp":

                datetime.utcnow().isoformat()

        }


        self.events.append(event)


        return event



    def summary(self):


        return {


            "usage_events":

                len(self.events),


            "events":

                self.events

        }