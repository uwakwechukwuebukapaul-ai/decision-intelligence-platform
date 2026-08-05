class MITREContext:
    """
    MITRE ATT&CK contextual mapping engine.
    """

    def map(self, behavior):

        mappings = []

        keywords = {
            "powershell": "T1059.001",
            "ransomware": "T1486",
            "credential": "T1003",
            "phishing": "T1566"
        }


        text = behavior.lower()


        for key, technique in keywords.items():

            if key in text:

                mappings.append(
                    {
                        "technique": technique,
                        "keyword": key
                    }
                )


        return mappings