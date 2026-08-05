class InvestigationDashboard:

    def __init__(self):
        self.views = []


    def create_view(self, investigation):

        view = {
            "investigation": investigation,
            "components": [
                "timeline",
                "entities",
                "evidence",
                "attack_path"
            ]
        }

        self.views.append(view)

        return view


    def list_views(self):

        return self.views