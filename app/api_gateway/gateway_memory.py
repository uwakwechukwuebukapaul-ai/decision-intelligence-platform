from datetime import datetime
import uuid


class GatewayMemory:


    def store(self, request_type, payload):

        return {

            "memory_id":

                "GW-" + str(uuid.uuid4())[:8].upper(),

            "request_type":

                request_type,

            "stored_payload":

                payload,

            "timestamp":

                datetime.utcnow().isoformat()

        }