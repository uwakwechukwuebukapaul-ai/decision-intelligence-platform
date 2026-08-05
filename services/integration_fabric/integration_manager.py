from .connectors import ConnectorRegistry
from .credential_manager import CredentialManager
from .connector_health import ConnectorHealth



class IntegrationManager:
    """
    Central integration control plane.

    Manages:
    - connectors
    - credentials
    - health monitoring
    """


    def __init__(self):

        self.registry = ConnectorRegistry()

        self.credentials = CredentialManager()

        self.health = ConnectorHealth()



    def connect(
        self,
        connector
    ):

        target = self.registry.get(
            connector
        )


        if not target:

            return {

                "status": "failed",

                "message":
                "Connector not found"

            }



        health = self.health.check(
            connector
        )


        return {

            "connector": target,

            "health": health,

            "status": "connected"

        }



    def available_integrations(self):

        return self.registry.list_connectors()