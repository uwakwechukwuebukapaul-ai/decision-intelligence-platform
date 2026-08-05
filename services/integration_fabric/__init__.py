from .connector_manager import ConnectorManager
from .siem_connector import SIEMConnector
from .edr_connector import EDRConnector
from .cloud_connector import CloudConnector
from .identity_connector import IdentityConnector
from .threat_feed_connector import ThreatFeedConnector
from .integration_gateway import IntegrationGateway


class IntegrationFabric:
    """
    Enterprise Integration Fabric

    Central communication layer between Sentinel DNA
    and external security platforms.
    """

    def __init__(self):
        self.connector_manager = ConnectorManager()
        self.gateway = IntegrationGateway()

        self.connectors = {
            "siem": SIEMConnector(),
            "edr": EDRConnector(),
            "cloud": CloudConnector(),
            "identity": IdentityConnector(),
            "threat_feed": ThreatFeedConnector(),
        }

    def register_connector(self, name, connector):
        self.connectors[name] = connector

    def get_connector(self, name):
        return self.connectors.get(name)

    def status(self):
        return {
            "service": "Integration Fabric",
            "connectors": list(self.connectors.keys()),
            "status": "ready"
        }