class HealthMonitor:

    def __init__(self):

        self.health = {}


    def check(self, service_registry):

        services = service_registry.list_services()

        for service in services:

            self.health[service] = {
                "status": "healthy"
            }

        return self.health


    def status(self):

        return self.health