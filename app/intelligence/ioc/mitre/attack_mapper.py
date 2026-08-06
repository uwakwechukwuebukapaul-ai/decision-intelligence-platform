"""
Sentinel DNA

MITRE ATT&CK IOC Mapper

Maps IOC intelligence signals
to possible ATT&CK techniques.

Foundation layer:
- Offline mapping
- Explainable output
- Future STIX/TAXII integration
"""

from __future__ import annotations



class AttackMapper:
    """
    MITRE ATT&CK mapping engine.
    """


    def map(
        self,
        indicator: dict,
    ) -> list:
        """
        Map IOC type to ATT&CK techniques.
        """


        indicator_type = indicator.get(
            "type",
            "unknown",
        )


        mappings = []


        if indicator_type == "domain":

            mappings.extend(

                [

                    {

                        "technique_id": "T1071.001",

                        "technique": "Web Protocols",

                        "reason": "Domain communication indicator",

                    },

                    {

                        "technique_id": "T1583.001",

                        "technique": "Domains",

                        "reason": "External domain infrastructure",

                    },

                ]

            )


        elif indicator_type == "ip":

            mappings.append(

                {

                    "technique_id": "T1071",

                    "technique": "Application Layer Protocol",

                    "reason": "Network indicator",

                }

            )


        return mappings