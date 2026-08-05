class IntelligenceCollector:

    def collect(self, source):

        return {
            "source": source,
            "data": [],
            "status": "collected"
        }

    def aggregate(self, feeds):

        return {
            "feeds": feeds,
            "total": len(feeds)
        }