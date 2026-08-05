class PatternEngine:

    def __init__(self):
        self.patterns = []

    def detect(self, event):

        pattern = {
            "event": event,
            "matched": True
        }

        self.patterns.append(pattern)

        return pattern

    def list_patterns(self):
        return self.patterns