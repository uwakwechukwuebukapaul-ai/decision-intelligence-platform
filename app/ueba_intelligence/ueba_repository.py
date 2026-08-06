class UEBARepository:


    def __init__(self):

        self.events = []



    def save(self, event):

        self.events.append(event)

        return event



    def get_all(self):

        return self.events