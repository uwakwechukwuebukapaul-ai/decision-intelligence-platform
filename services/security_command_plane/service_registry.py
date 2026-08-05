class ServiceRegistry:
    """
    Registers Sentinel DNA services.
    """

    def __init__(self):
        self.services = {}


    def register(self, name, service):

        self.services[name] = {
            "service": service,
            "status": "active"
        }

        return self.services[name]


    def get_service(self, name):

        return self.services.get(name)


    def list_services(self):

        return self.services