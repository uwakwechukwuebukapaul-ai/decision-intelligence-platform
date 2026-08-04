class MemoryStore:


    def __init__(self):

        self.entities = []

        self.threats = []

        self.cases = []

        self.intelligence = []



    def store_entity(
        self,
        entity
    ):

        self.entities.append(
            entity
        )

        return entity



    def store_threat(
        self,
        threat
    ):

        self.threats.append(
            threat
        )

        return threat



    def store_case(
        self,
        case
    ):

        self.cases.append(
            case
        )

        return case



    def store_intelligence(
        self,
        intelligence
    ):

        self.intelligence.append(
            intelligence
        )

        return intelligence



    def get_entities(self):

        return self.entities



    def get_threats(self):

        return self.threats



    def get_cases(self):

        return self.cases



    def get_intelligence(self):

        return self.intelligence