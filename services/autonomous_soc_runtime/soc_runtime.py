class SOCRuntime:
    """
    Core runtime controller.
    """

    def start(self):

        return {
            "runtime": "started",
            "status": "active"
        }


    def stop(self):

        return {
            "runtime": "stopped"
        }