from datetime import datetime
import hashlib


class KnowledgeMemory:
    """
    Secure knowledge retention layer.
    """

    def __init__(self):

        self.storage = []


    def store(self, knowledge):

        fingerprint = hashlib.sha256(
            str(knowledge).encode()
        ).hexdigest()


        record = {

            "knowledge_id":
                "KNOW-" + fingerprint[:8],

            "knowledge":
                knowledge,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.storage.append(record)

        return record


    def history(self):

        return {

            "count":
                len(self.storage),

            "records":
                self.storage

        }