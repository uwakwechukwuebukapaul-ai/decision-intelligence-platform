from datetime import datetime


class AnomalyDetector:

    def detect(self, event):

        anomalies = []

        keywords = [
            "ransomware",
            "powershell",
            "database",
            "attack"
        ]

        for keyword in keywords:
            if keyword in event.lower():
                anomalies.append(keyword)

        return {
            "anomalies_detected": anomalies,
            "anomaly_score": len(anomalies) * 25,
            "timestamp": datetime.now().isoformat()
        }