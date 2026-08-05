class AttackPathEngine:
    def __init__(self):
        self.paths = []

    def analyze_path(self, source, target):
        path = {
            "source": source,
            "target": target,
            "risk": "unknown",
            "steps": []
        }

        self.paths.append(path)

        return path

    def add_step(self, path, technique):
        path["steps"].append(technique)

        return path

    def get_paths(self):
        return self.paths