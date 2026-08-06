from datetime import datetime


class ResponseRepository:


    def __init__(self):

        self.responses = []



    def save(
        self,
        response: dict
    ):

        self.responses.append(response)

        return response



    def list_all(self):

        return self.responses