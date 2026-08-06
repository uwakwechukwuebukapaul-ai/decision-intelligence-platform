class MITRERepository:

    def __init__(self):

        self.mappings = []

    def save(self, mapping):

        self.mappings.append(mapping)

        return mapping

    def get_all(self):

        return self.mappings

    def find_by_indicator(self, indicator):

        return [
            mapping
            for mapping in self.mappings
            if mapping["indicator"] == indicator
        ]