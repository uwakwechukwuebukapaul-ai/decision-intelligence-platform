class IntegrationGateway:
    """
    Unified gateway for all external communication.
    """

    def __init__(self):
        self.requests = []

    def send(self, target, payload):
        request = {
            "target": target,
            "payload": payload,
            "status": "queued"
        }

        self.requests.append(request)

        return request

    def history(self):
        return self.requests