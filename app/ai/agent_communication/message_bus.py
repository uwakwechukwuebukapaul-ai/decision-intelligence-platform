from datetime import datetime


class MessageBus:


    def __init__(self):

        self.messages = []



    def send_message(
        self,
        sender,
        receiver,
        message,
        message_type="intelligence"
    ):


        payload = {


            "sender": sender,


            "receiver": receiver,


            "message_type": message_type,


            "message": message,


            "timestamp":

                datetime.utcnow().isoformat()


        }


        self.messages.append(payload)


        return payload




    def get_messages(self):

        return self.messages




    def clear_messages(self):

        self.messages = []

        return True