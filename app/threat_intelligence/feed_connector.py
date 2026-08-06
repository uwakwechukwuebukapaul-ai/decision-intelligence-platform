class FeedConnector:

    def get_feeds(self):

        return [
            {
                "source": "internal_feed",
                "status": "active",
                "indicators": []
            },
            {
                "source": "open_threat_feed",
                "status": "ready",
                "indicators": []
            }
        ]


    def ingest(self, indicators):

        return {
            "status": "completed",
            "ingested": len(indicators),
            "indicators": indicators
        }