class DetectionRepository:


    def __init__(self):

        self.records = []


    def save(self, detection):

        self.records.append(detection)

        return detection


    def all(self):

        return self.records