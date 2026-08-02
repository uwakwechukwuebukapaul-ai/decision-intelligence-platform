"""
AI Agent Communication Bus

Responsible for:
- Agent messaging
- Shared intelligence exchange
- Collaboration events
"""


from datetime import datetime



class CommunicationBus:


    def __init__(self):

        self.messages = []



    def send_message(
        self,
        sender,
        receiver,
        message
    ):

        event = {

            "sender": sender,

            "receiver": receiver,

            "message": message,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.messages.append(event)


        return event



    def broadcast(
        self,
        sender,
        agents,
        message
    ):

        events = []


        for agent in agents:

            events.append(

                self.send_message(

                    sender,

                    agent,

                    message

                )

            )


        return events



    def get_messages(self):

        return self.messages



    def status(self):

        return {


            "communication_bus":

                "active",


            "messages":

                len(self.messages)

        }