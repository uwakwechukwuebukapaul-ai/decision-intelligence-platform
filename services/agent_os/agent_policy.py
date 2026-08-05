class AgentPolicy:
    """
    Autonomous agent governance layer.

    Controls permissions and autonomy levels.
    """


    def __init__(self):

        self.policies = {}


    def create_policy(
        self,
        agent,
        autonomy_level,
        permissions
    ):

        self.policies[agent] = {

            "agent":
                agent,

            "autonomy_level":
                autonomy_level,

            "permissions":
                permissions

        }


        return self.policies[agent]


    def get_policy(
        self,
        agent
    ):

        return self.policies.get(
            agent
        )


    def allowed(
        self,
        agent,
        action
    ):

        policy = self.get_policy(
            agent
        )


        if not policy:

            return False


        return action in policy["permissions"]