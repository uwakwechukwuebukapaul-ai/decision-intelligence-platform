"""
Sentinel DNA
Investigation Memory

Stores investigation intelligence records.
"""


class InvestigationMemoryRecord:

    def __init__(
        self,
        investigation_id,
        data,
    ):

        self.investigation_id = investigation_id

        self.data = data



class InvestigationMemory:

    def __init__(self):

        self.memory = {}



    def remember(
        self,
        investigation_id,
        data,
    ):
        """
        Store investigation intelligence.
        """

        record = InvestigationMemoryRecord(
            investigation_id,
            data,
        )


        self.memory[investigation_id] = record


        return record



    def recall(
        self,
        investigation_id,
    ):
        """
        Retrieve investigation record.
        """

        return self.memory.get(
            investigation_id
        )



    def clear(
        self,
        investigation_id=None,
    ):
        """
        Clear stored investigations.
        """

        if investigation_id:

            self.memory.pop(
                investigation_id,
                None
            )

        else:

            self.memory.clear()



    def list_investigations(
        self,
    ):

        return list(
            self.memory.keys()
        )