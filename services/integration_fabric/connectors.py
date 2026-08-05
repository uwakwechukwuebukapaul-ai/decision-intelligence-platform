class ConnectorRegistry:
    """
    Sentinel DNA external connector registry.

    Future integrations:
    - EDR
    - SIEM
    - Firewall
    - Cloud
    - Identity providers
    """


    def __init__(self):

        self.connectors = {

            "edr": {
                "name": "Endpoint Detection Response",
                "status": "available"
            },


            "siem": {
                "name": "Security Information Event Management",
                "status": "available"
            },


            "firewall": {
                "name": "Network Firewall",
                "status": "available"
            },


            "identity": {
                "name": "Identity Provider",
                "status": "available"
            },


            "cloud": {
                "name": "Cloud Security Provider",
                "status": "available"
            }

        }


    def register(
        self,
        name,
        metadata
    ):

        self.connectors[name] = metadata


    def get(
        self,
        name
    ):

        return self.connectors.get(name)


    def list_connectors(self):

        return self.connectors