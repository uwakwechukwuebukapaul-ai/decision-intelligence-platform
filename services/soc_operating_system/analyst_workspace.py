class AnalystWorkspace:
    """
    Provides analyst operational workspace abstraction.
    """

    def __init__(self):
        self.sessions = {}

    def create_session(self, analyst_id):

        self.sessions[analyst_id] = {
            "analyst_id": analyst_id,
            "active_cases": [],
            "notes": [],
        }

        return self.sessions[analyst_id]

    def add_case(self, analyst_id, case_id):

        if analyst_id not in self.sessions:
            self.create_session(analyst_id)

        self.sessions[analyst_id]["active_cases"].append(case_id)

        return self.sessions[analyst_id]