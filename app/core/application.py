"""
Application Runtime Bootstrap

Coordinates application startup lifecycle.
"""

from app.core.container import container


class ApplicationRuntime:
    """
    Manages application lifecycle.

    Responsibilities:
    - initialize services
    - expose runtime health
    - expose service state
    - prepare shutdown hooks
    """

    def __init__(self):

        self.started = False


    def start(self):
        """
        Start application services.
        """

        if self.started:
            return

        container.initialize()

        self.started = True



    def status(self):
        """
        Runtime status information.
        """

        return {
            "application": "Decision Intelligence Platform",
            "runtime": (
                "active"
                if self.started
                else "inactive"
            ),
            "started": self.started,
        }



    def health(self):
        """
        Runtime health information.
        """

        return {
            "runtime": (
                "healthy"
                if self.started
                else "not_started"
            ),

            "container": container.health(),
        }



    def services(self):
        """
        Service availability information.
        """

        return container.health().get(
            "services",
            {}
        )



    def shutdown(self):
        """
        Graceful shutdown hook.
        """

        self.started = False



runtime = ApplicationRuntime()