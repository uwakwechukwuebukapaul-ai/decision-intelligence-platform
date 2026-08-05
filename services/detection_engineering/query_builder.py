class QueryBuilder:
    """
    Generates SIEM-compatible detection queries.
    """

    def build(self, pattern):

        technique = pattern.get(
            "technique"
        )

        if technique == "T1059.001":

            return {
                "platform": "generic-siem",
                "query":
                    'process_name="powershell.exe"'
            }

        if technique == "T1003":

            return {
                "platform": "generic-siem",
                "query":
                    'event.category="credential_access"'
            }

        return {
            "platform": "generic-siem",
            "query": "unknown"
        }