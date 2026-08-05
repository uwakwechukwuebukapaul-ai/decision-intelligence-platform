class SOCRuntime:

    def __init__(self):

        self.running = False


    def start(self):

        self.running = True

        return {
            "runtime": "SOC Runtime",
            "status": "active"
        }


    def stop(self):

        self.running = False

        return {
            "status": "stopped"
        }


    def health(self):

        return {
            "running": self.running
        }