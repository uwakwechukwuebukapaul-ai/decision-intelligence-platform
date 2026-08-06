from app.intelligence.kernel.intelligence_services import IntelligenceServices


class ServiceFactory:

    @staticmethod
    def create():
        return IntelligenceServices()