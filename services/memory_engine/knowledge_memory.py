from datetime import datetime, timezone


class KnowledgeMemory:
    """
    Sentinel DNA Security Knowledge Memory.

    Long-term intelligence storage layer.

    Stores:

    - MITRE ATT&CK knowledge
    - Threat intelligence
    - Security concepts
    - Investigation learnings
    - Attack patterns
    """


    def __init__(
        self,
        store=None
    ):

        self.store = store

        self.local_memory = []



    def add(
        self,
        knowledge
    ):

        record = {

            "type":
                "knowledge",

            "data":
                knowledge,

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.local_memory.append(
            record
        )


        if self.store:

            return self.store.store(
                "knowledge",
                record
            )


        return record



    def add_investigation_learning(
        self,
        investigation
    ):
        """
        Store completed investigation intelligence.

        Used for future SOC reasoning.
        """


        record = {

            "type":
                "investigation_learning",

            "investigation":
                investigation,

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.local_memory.append(
            record
        )


        if self.store:

            return self.store.store(
                "investigation_learning",
                record
            )


        return record



    def query(
        self,
        keyword
    ):

        if self.store:

            return self.store.search(
                keyword
            )


        results = []


        for item in self.local_memory:

            if keyword.lower() in str(
                item
            ).lower():

                results.append(
                    item
                )


        return results



    def retrieve_similar_investigations(
        self,
        threat_pattern
    ):
        """
        Retrieve previous investigations
        matching threat behaviour.
        """


        matches = []


        for item in self.local_memory:

            if item.get(
                "type"
            ) != "investigation_learning":

                continue


            if threat_pattern.lower() in str(
                item
            ).lower():

                matches.append(
                    item
                )


        return matches



    def all_memory(
        self
    ):

        return self.local_memory