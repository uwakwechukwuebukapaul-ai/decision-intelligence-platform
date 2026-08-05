"""
Decision Core Adapter
"""


def decision_core_capability(context, **kwargs):

    return {

        "capability":
            "decision_core",

        "status":
            "available",

        "decision":
            "Decision intelligence initialized",

        "user":
            context.user_id

    }