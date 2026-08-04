from datetime import datetime


class ContainmentActions:

    def execute(self, incident):

        return [
            "Isolate compromised systems",
            "Disable compromised accounts",
            "Block malicious indicators",
            "Restrict attacker access"
        ]