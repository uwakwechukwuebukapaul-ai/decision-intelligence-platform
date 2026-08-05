class CredentialManager:
    """
    Secure credential abstraction.

    Production version:
    - Hashicorp Vault
    - AWS Secrets Manager
    - Azure Key Vault
    """


    def __init__(self):

        self.credentials = {}


    def store(
        self,
        service,
        credential
    ):

        self.credentials[service] = credential


    def retrieve(
        self,
        service
    ):

        return self.credentials.get(service)


    def remove(
        self,
        service
    ):

        if service in self.credentials:

            del self.credentials[service]