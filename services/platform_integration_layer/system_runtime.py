class SystemRuntime:

    def __init__(self):
        self.running = False


    def start(self):

        self.running = True

        return {
            "runtime": "started",
            "status": "running"
        }


    def stop(self):

        self.running = False

        return {
            "runtime": "stopped",
            "status": "offline"
        }


    def status(self):

        return {
            "running": self.running
        }