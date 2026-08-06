class AnomalyDetector:


    def detect(
        self,
        behavior
    ):

        anomalies = []


        if not behavior["normal"]:

            anomalies.append(
                "Unusual login behavior"
            )


        return anomalies