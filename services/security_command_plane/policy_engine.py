class PolicyEngine:
    """
    Security automation policy enforcement.
    """

    def __init__(self):
        self.policies = []


    def create_policy(self, name, rule):

        policy = {
            "name": name,
            "rule": rule,
            "enabled": True
        }

        self.policies.append(policy)

        return policy


    def evaluate(self, context):

        return {
            "context": context,
            "decision": "allowed"
        }


    def list_policies(self):

        return self.policies