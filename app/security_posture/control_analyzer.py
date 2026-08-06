class ControlAnalyzer:

    def analyze(self, signals):
        controls = []

        controls.append({
            "control": "Threat Detection",
            "status": "enabled" if not signals.get("detection_gap") else "needs_improvement"
        })

        controls.append({
            "control": "Identity Protection",
            "status": "risk" if signals.get("identity_risk") else "healthy"
        })

        controls.append({
            "control": "Asset Protection",
            "status": "risk" if signals.get("asset_exposure") else "healthy"
        })

        return controls