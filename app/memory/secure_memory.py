import hashlib
import json
from datetime import datetime



class SecureMemory:


    def __init__(self):

        self.secret = "sentinel-dna-memory-key"



    def encrypt(self, data):

        payload = json.dumps(
            data,
            sort_keys=True
        )

        encrypted = hashlib.sha256(
            (
                self.secret +
                payload
            ).encode()
        ).hexdigest()


        return {


            "hash":
                encrypted,


            "created_at":
                datetime.utcnow().isoformat()

        }



    def verify(self, data, stored_hash):

        payload = json.dumps(
            data,
            sort_keys=True
        )


        current_hash = hashlib.sha256(
            (
                self.secret +
                payload
            ).encode()
        ).hexdigest()


        return current_hash == stored_hash