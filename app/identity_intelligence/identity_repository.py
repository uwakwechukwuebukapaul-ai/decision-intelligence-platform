class IdentityRepository:


    def __init__(self):

        self.identities = []


    def save(self, identity):

        self.identities.append(identity)

        return identity


    def get_all(self):

        return self.identities


    def find(self, username):

        for identity in self.identities:

            if identity["username"] == username:
                return identity

        return None