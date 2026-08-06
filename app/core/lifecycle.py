"""
Platform Lifecycle Management

Coordinates startup and shutdown lifecycle
for the Decision Intelligence Platform.
"""


from app.core.application import runtime


class PlatformLifecycle:
    """
    Enterprise lifecycle controller.

    Responsibilities:
    - startup orchestration
    - runtime health monitoring
    - graceful shutdown
    """

    def __init__(self):

        self.started = False



    def startup(self):
        """
        Start platform services.
        """

        if self.started:
            return


        runtime.start()

        self.started = True



    def health(self):
        """
        Return lifecycle health state.
        """

        return {
            "lifecycle": (
                "healthy"
                if self.started
                else "not_started"
            ),
            "runtime": runtime.health(),
        }



    def shutdown(self):
        """
        Shutdown platform services.
        """

        runtime.shutdown()

        self.started = False



lifecycle = PlatformLifecycle()