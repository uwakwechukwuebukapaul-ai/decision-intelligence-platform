class FeedManager:

    def __init__(self):
        self.feeds = [
            "offline_feed"
        ]


    def register_feed(self, name):

        self.feeds.append(name)

        return {
            "status": "registered",
            "feed": name
        }


    def list_feeds(self):

        return self.feeds