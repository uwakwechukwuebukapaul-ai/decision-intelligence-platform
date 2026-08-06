"""
Sentinel DNA Threat Intelligence Manager
"""


from .providers import (
    OfflineThreatProvider,
)

from .intelligence_repository import (
    IntelligenceRepository,
)

from .intelligence_schema import (
    IntelligenceRecord,
)



class IntelligenceManager:



    def __init__(self):

        self.provider = (
            OfflineThreatProvider()
        )

        self.repository = (
            IntelligenceRepository()
        )



    def enrich(
        self,
        ioc: str,
    ):


        result = (
            self.provider
            .analyze(
                ioc
            )
        )


        record = IntelligenceRecord(

            ioc=ioc,

            reputation_score=result[
                "reputation_score"
            ],

            threat_level=result[
                "threat_level"
            ],

            details={
                "reasons":
                    result["reasons"]
            },

            source=result[
                "source"
            ],
        )


        return self.repository.save(
            record.to_dict()
        )



    def get_intelligence(
        self,
        ioc,
    ):

        return self.repository.get(
            ioc
        )