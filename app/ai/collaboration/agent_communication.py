from datetime import datetime
import uuid


class AgentCommunication:

    def __init__(self):

        self.messages = []


    def send_message(
        self,
        sender,
        receiver,
        content
    ):

        message = {

            "message_id":
                f"MSG-{uuid.uuid4().hex[:8].upper()}",

            "sender":
                sender,

            "receiver":
                receiver,

            "content":
                content,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.messages.append(message)


        return message



    def get_messages(
        self,
        agent_id
    ):

        results = []


        for message in self.messages:

            if (
                message["sender"] == agent_id
                or
                message["receiver"] == agent_id
            ):

                results.append(message)


        return {

            "agent_id":
                agent_id,

            "message_count":
                len(results),

            "messages":
                results

        }