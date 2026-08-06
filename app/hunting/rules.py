"""
Sentinel DNA Hunting Rules

Initial threat hunting rules.
"""


HUNT_RULES = {


    "suspicious_domain":

    {

        "description":
            "Detect suspicious domain indicators",

        "severity":
            "high"

    },


    "malicious_ip":

    {

        "description":
            "Detect known malicious IP activity",

        "severity":
            "critical"

    },


    "credential_activity":

    {

        "description":
            "Detect suspicious authentication behavior",

        "severity":
            "high"

    }

}