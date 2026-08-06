class DetectionRepository:


    def __init__(self):

        self.detections = []



    def save(self, detection):

        self.detections.append(
            detection
        )

        return detection



    def get_all(self):

        return self.detections



    def get_by_indicator(
        self,
        indicator
    ):

        return [
            item
            for item in self.detections
            if item["indicator"] == indicator
        ]