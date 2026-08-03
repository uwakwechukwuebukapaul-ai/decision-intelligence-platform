from datetime import datetime


class PerceptionLayer:
    """
    Collects and interprets incoming security signals.
    """

    def perceive(self, input_data):

        text = str(input_data).lower()

        signals = []

        indicators = [
            "ransomware",
            "malware",
            "phishing",
            "powershell",
            "credential",
            "lateral movement"
        ]

        for indicator in indicators:
            if indicator in text:
                signals.append(indicator)


        return {
            "signals_detected": signals,
            "signal_count": len(signals),
            "timestamp": datetime.utcnow().isoformat()
        }