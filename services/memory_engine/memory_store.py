from datetime import datetime, timezone


class MemoryStore:
    """
    Sentinel DNA Long-Term Memory Storage Core.

    Supports:

    - In-memory operation (legacy mode)
    - Persistent repository storage
    - Future database/vector integrations

    Backward compatible with existing
    MemoryEngine components.
    """


    def __init__(
        self,
        repository=None
    ):

        self.repository = repository

        # Legacy runtime cache
        self.records = []



    def store(
        self,
        memory_type,
        data
    ):

        record = {

            "type":
                memory_type,

            "data":
                data,

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        # Persistent storage mode

        if self.repository:

            return self.repository.store(
                memory_type,
                data
            )


        # Legacy memory mode

        self.records.append(
            record
        )


        return record



    def get_all(
        self
    ):


        if self.repository:

            return self.repository.get_all()


        return self.records



    def search(
        self,
        keyword
    ):


        if self.repository:

            return self.repository.search(
                keyword
            )


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



    def count(
        self
    ):

        memories = self.get_all()

        return len(
            memories
        )