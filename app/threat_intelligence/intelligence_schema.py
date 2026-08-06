"""
Sentinel DNA Threat Intelligence Schemas
"""


from datetime import datetime



class IntelligenceRecord:


    def __init__(
        self,
        ioc,
        ioc_type="domain",
        reputation_score=0,
        threat_level="unknown",
        source="offline",
        details=None,
    ):

        self.ioc = ioc

        self.ioc_type = ioc_type

        self.reputation_score = (
            reputation_score
        )

        self.threat_level = (
            threat_level
        )

        self.source = source

        self.details = (
            details or {}
        )

        self.created_at = (
            datetime.utcnow()
            .isoformat()
        )



    def to_dict(self):

        return {

            "ioc":
                self.ioc,

            "ioc_type":
                self.ioc_type,

            "reputation_score":
                self.reputation_score,

            "threat_level":
                self.threat_level,

            "source":
                self.source,

            "details":
                self.details,

            "created_at":
                self.created_at,

        }