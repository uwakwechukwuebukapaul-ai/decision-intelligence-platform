from datetime import datetime
import uuid


class InvestigationMemory:
    """
    Central Investigation Memory Store.

    Responsible for:
    - storing investigations
    - retrieving investigation history
    - searching previous investigations
    - supporting future AI learning loops
    """

    def __init__(self):

        self.investigations = []


    def store_investigation(
        self,
        investigation
    ):

        record = {

            "memory_id":
                f"MEM-{uuid.uuid4().hex[:8].upper()}",

            "type":
                "investigation",

            "data":
                investigation,

            "learned_patterns":[

                "Evidence collection",

                "IOC enrichment",

                "Timeline reconstruction",

                "Threat classification"

            ],

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.investigations.append(
            record
        )


        return record



    def retrieve_all(
        self
    ):

        return self.investigations



    def search(
        self,
        keyword
    ):

        results = []


        for investigation in self.investigations:

            if keyword.lower() in str(
                investigation
            ).lower():

                results.append(
                    investigation
                )


        return results



    def latest(
        self
    ):

        if self.investigations:

            return self.investigations[-1]


        return None



    def count(
        self
    ):

        return len(
            self.investigations
        )