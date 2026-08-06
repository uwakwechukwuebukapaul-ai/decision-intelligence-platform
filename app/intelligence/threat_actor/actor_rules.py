"""
Sentinel DNA - Threat Actor Detection Rules
"""


ACTOR_RULES = [

    {

        "name":
        "Unknown Command Infrastructure Cluster",


        "techniques":
        [
            "T1071.001",
            "T1583.001",
        ],


        "confidence":
        65,


        "reasoning":
        [
            "Web protocol communication",
            "External domain infrastructure",
        ],

    },


]