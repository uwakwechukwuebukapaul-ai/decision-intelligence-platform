class HuntRepository:


    def __init__(self):

        self.hunts = []



    def save(
        self,
        hunt
    ):

        self.hunts.append(
            hunt
        )

        return hunt



    def get_all(self):

        return self.hunts



    def get_by_indicator(
        self,
        indicator
    ):

        return [

            hunt

            for hunt in self.hunts

            if hunt["indicator"] == indicator

        ]