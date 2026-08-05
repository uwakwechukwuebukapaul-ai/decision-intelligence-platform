class ServiceMesh:

    def __init__(self):
        self.services = {}

    def register_service(self, name, service):
        self.services[name] = service
        return {
            "status": "registered",
            "service": name
        }

    def get_service(self, name):
        return self.services.get(name)

    def list_services(self):
        return list(self.services.keys())

    def health(self):
        return {
            "component": "service_mesh",
            "status": "healthy",
            "services": len(self.services)
        }