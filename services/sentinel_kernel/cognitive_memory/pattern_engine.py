class PatternEngine:
    """
    Detects recurring security patterns.

    Example:
    - repeated malware indicators
    - repeated attack techniques
    - recurring behaviors
    """

    def analyze(
        self,
        event
    ):

        patterns = []

        text = str(event).lower()


        indicators = {

            "powershell":
                "command_execution",

            "ransomware":
                "data_encryption_attack",

            "credential":
                "credential_compromise",

            "phishing":
                "initial_access"

        }


        for keyword, pattern in indicators.items():

            if keyword in text:

                patterns.append(
                    pattern
                )


        return patterns