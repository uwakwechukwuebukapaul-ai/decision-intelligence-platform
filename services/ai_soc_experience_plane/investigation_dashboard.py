class InvestigationDashboard:
    """
    Sentinel DNA investigation visualization workspace.

    Provides:
    - investigation views
    - timeline visualization
    - evidence mapping
    - entity relationships
    """

    def __init__(self):
        self.investigations = []


    def create_view(self, investigation):

        view = {
            "investigation": investigation,
            "components": [
                "timeline",
                "evidence",
                "entities",
                "attack_path"
            ],
            "status": "active"
        }

        self.investigations.append(view)

        return view


    def get_view(self, investigation_id):

        for view in self.investigations:
            if view.get("investigation") == investigation_id:
                return view

        return None


    def list_views(self):

        return self.investigations