"""
MITRE ATT&CK mapping engine.
"""


class MitreMapper:


    def map_indicator(
        self,
        indicator
    ):

        techniques = []


        if "." in indicator:

            techniques.append(
                "T1583.001 - Acquire Infrastructure: Domains"
            )


        return techniques