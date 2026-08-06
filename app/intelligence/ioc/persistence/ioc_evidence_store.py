"""
Sentinel DNA

IOC Evidence Store

Stores investigation evidence:
- Risk
- Reputation
- MITRE mapping
- Threat context
"""


class IOCEvidenceStore:
    """
    IOC evidence storage.
    """


    def __init__(self):

        self.evidence = {}



    def store(
        self,
        indicator: str,
        evidence: dict,
    ) -> dict:
        """
        Store IOC evidence.
        """


        record = {

            "indicator": indicator,

            "evidence": evidence,

        }


        self.evidence[indicator] = record


        return record



    def retrieve(
        self,
        indicator: str,
    ) -> dict | None:


        return self.evidence.get(
            indicator
        )