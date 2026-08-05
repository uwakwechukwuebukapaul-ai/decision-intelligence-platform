from collections import Counter


class PatternEngine:

    def __init__(self):
        self.patterns = []

    def analyze(self, events):

        counter = Counter(
            str(event.get("type", "unknown"))
            for event in events
        )

        result = {
            "patterns_detected": dict(counter),
            "total_events": len(events)
        }

        self.patterns.append(result)

        return result

    def get_patterns(self):

        return self.patterns