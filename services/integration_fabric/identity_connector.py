class IdentityConnector:
    """
    Identity security connector.

    Future:
    - Active Directory
    - Azure AD
    - Okta
    """

    def __init__(self):
        self.name = "Identity"

    def get_user_activity(self, user):
        return {
            "user": user,
            "activity": []
        }

    def investigate_account(self, account):
        return {
            "account": account,
            "risk": "unknown"
        }