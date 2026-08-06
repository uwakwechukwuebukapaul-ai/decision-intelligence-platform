class BehaviorRepository:


    def __init__(self):

        self.events = []



    def save(self,event):

        self.events.append(event)

        return event



    def get_user_events(self,username):

        return [
            e for e in self.events
            if e["username"] == username
        ]