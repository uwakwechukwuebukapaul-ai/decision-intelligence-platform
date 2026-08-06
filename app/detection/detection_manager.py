from .detection_engine import DetectionEngine
from .detection_repository import DetectionRepository



class DetectionManager:


    def __init__(self):

        self.engine = DetectionEngine()

        self.repository = DetectionRepository()



    def detect(
        self,
        indicator
    ):


        results = self.engine.analyze(
            indicator
        )


        saved = []


        for detection in results:

            saved.append(

                self.repository.save(
                    detection
                )

            )


        return saved