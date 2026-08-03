class DecisionHistory:


    def __init__(self):

        self.decisions = []



    def add_decision(
        self,
        mission_id,
        decision
    ):

        record = {

            "mission_id": mission_id,

            "decision": decision

        }


        self.decisions.append(record)


        return record



    def get_history(
        self,
        mission_id=None
    ):

        if mission_id:

            return [

                item

                for item in self.decisions

                if item["mission_id"] == mission_id

            ]


        return self.decisions