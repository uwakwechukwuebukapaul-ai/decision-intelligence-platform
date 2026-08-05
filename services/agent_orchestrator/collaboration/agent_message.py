from datetime import datetime
import uuid


class AgentMessage:
    """
    Standard communication object
    between Sentinel DNA autonomous agents.
    """


    def __init__(
        self,
        sender,
        receiver,
        action,
        payload
    ):

        self.id = str(uuid.uuid4())

        self.sender = sender

        self.receiver = receiver

        self.action = action

        self.payload = payload

        self.timestamp = datetime.utcnow()



    def to_dict(self):

        return {

            "message_id": self.id,

            "sender": self.sender,

            "receiver": self.receiver,

            "action": self.action,

            "payload": self.payload,

            "timestamp": self.timestamp.isoformat()

        }