class MemoryStore:
    """
    Sentinel DNA Long-Term Memory Storage Core.

    Provides persistent in-memory abstraction
    for future database/vector integration.
    """


    def __init__(self):

        self.records = []


    def store(
        self,
        memory_type,
        data
    ):

        record = {

            "type": memory_type,

            "data": data

        }


        self.records.append(record)


        return record



    def get_all(
        self
    ):

        return self.records



    def search(
        self,
        keyword
    ):

        results = []


        keyword = keyword.lower()


        for record in self.records:

            content = str(
                record
            ).lower()


            if keyword in content:

                results.append(
                    record
                )


        return results