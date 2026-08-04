class ServiceRegistry:

    def __init__(self):
        self.services = {}


    def register(self, name, service):

        self.services[name] = {
            "service": service,
            "status": "registered"
        }

        return self.services[name]


    def get(self, name):

        return self.services.get(name)


    def list_services(self):

        return list(self.services.keys())