class VisualizationEngine:

    def __init__(self):
        self.visualizations = []


    def create_visualization(self, data):

        view = {
            "data": data,
            "type": "security_visualization"
        }

        self.visualizations.append(view)

        return view


    def list_visualizations(self):

        return self.visualizations