from datetime import datetime


class SecurityPolicy:
    """
    Gateway security enforcement rules.
    """


    def evaluate(self, request):

        blocked_keywords = [

            "malware",
            "exploit",
            "unauthorized"

        ]


        text = str(request).lower()


        violations = [

            item
            for item in blocked_keywords
            if item in text

        ]


        return {

            "allowed":
                len(violations) == 0,

            "violations":
                violations,

            "timestamp":
                datetime.utcnow().isoformat()

        }