class AdversaryModel:
    """
    Represents attacker behavior profiles.
    """


    def create_profile(
        self,
        actor,
        capabilities=None
    ):

        return {

            "actor": actor,

            "capabilities": capabilities or [],

            "behavior": {

                "stealth": True,

                "persistence": True,

                "adaptation": True

            },

            "status": "profile_created"

        }