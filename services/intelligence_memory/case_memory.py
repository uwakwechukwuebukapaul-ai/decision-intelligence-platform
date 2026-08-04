import uuid


class CaseMemory:


    def __init__(self, store):

        self.store = store



    def remember_case(
        self,
        incident,
        resolution
    ):


        case = {

            "id":
                f"CASE-{uuid.uuid4().hex[:8].upper()}",

            "incident":
                incident,

            "resolution":
                resolution

        }


        return self.store.store_case(case)