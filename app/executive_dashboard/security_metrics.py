class SecurityMetrics:

    def calculate(self, data):
        metrics = {
            "critical_threats": data.get("critical_threats", 0),
            "active_incidents": data.get("active_incidents", 0),
            "vulnerabilities": data.get("vulnerabilities", 0),
            "identity_risks": data.get("identity_risks", 0),
            "asset_exposure": data.get("asset_exposure", 0),
            "detection_coverage": data.get("detection_coverage", 0)
        }

        return metrics