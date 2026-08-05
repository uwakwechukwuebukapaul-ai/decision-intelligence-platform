class IntelligenceRouter:

    def __init__(self):

        self.routes = {}


    def register_route(self, name, handler):

        self.routes[name] = handler


    def route(self, destination, data):

        handler = self.routes.get(destination)

        if handler:

            return handler(data)


        return {
            "destination": destination,
            "data": data
        }