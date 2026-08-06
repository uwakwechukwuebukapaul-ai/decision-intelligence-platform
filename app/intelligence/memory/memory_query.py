"""
Sentinel DNA Memory Query Engine
"""


class MemoryQuery:


    def __init__(
        self,
        store,
    ):

        self.store = store



    def search_indicator(
        self,
        indicator,
    ):

        records = self.store.find(
            indicator
        )


        return [

            record.to_dict()

            for record in records

        ]



    def exists(
        self,
        indicator,
    ):

        return len(
            self.store.find(indicator)
        ) > 0