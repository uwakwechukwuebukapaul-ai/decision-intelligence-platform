class AnomalyEngine:

    def detect(self, data):

        return {
            "anomaly_found": False,
            "data": data
        }


    def score(self, event):

        return 0