"""
Sentinel DNA - Threat Actor Query Layer
"""





class ThreatActorQuery:


    def search(
        self,
        records,
        indicator,
    ):


        return [

            item

            for item in records

            if item.get(
                "indicator"
            )
            == indicator

        ]