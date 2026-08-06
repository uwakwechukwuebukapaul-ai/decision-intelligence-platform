from uuid import uuid4


class MemoryRepository:


    def __init__(self):

        self.records = []



    def save(self, memory):

        self.records.append(memory)

        return memory



    def find_by_indicator(self, indicator):

        return [
            item for item in self.records
            if item.indicator == indicator
        ]



    def all(self):

        return self.records