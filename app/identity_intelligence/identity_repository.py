class IdentityRepository:


    def __init__(self):

        self.identities = {}



    def save(self, identity):

        self.identities[
            identity["username"]
        ] = identity

        return identity



    def get(self, username):

        return self.identities.get(username)