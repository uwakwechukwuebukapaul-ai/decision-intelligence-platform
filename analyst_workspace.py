class AnalystWorkspace:

    def __init__(self):
        self.sessions = []


    def create_session(self, analyst):

        session = {
            "analyst": analyst,
            "status": "active"
        }

        self.sessions.append(session)

        return session


    def list_sessions(self):

        return self.sessions