class PlatformController:
    """
    Controls Sentinel DNA platform lifecycle.
    """

    def __init__(self):
        self.state = "stopped"


    def start(self):

        self.state = "running"

        return {
            "status": self.state
        }


    def stop(self):

        self.state = "stopped"

        return {
            "status": self.state
        }


    def status(self):

        return {
            "platform": self.state
        }