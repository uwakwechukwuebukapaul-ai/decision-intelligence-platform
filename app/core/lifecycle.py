"""
Platform Lifecycle Management

Coordinates startup and shutdown lifecycle
for the Decision Intelligence Platform.
"""

from __future__ import annotations


class PlatformLifecycle:
    """
    Manages platform lifecycle state.

    Responsibilities:
    - startup orchestration
    - shutdown handling
    - lifecycle health reporting
    """

    def __init__(self):

        self.started = False


    def startup(self):
        """
        Initialize platform lifecycle.

        Backward compatible API expected by tests
        and future platform services.
        """

        if self.started:
            return

        self.started = True



    def start(self):
        """
        Alias for startup.

        Keeps compatibility with application factory.
        """

        self.startup()



    def shutdown(self):
        """
        Graceful lifecycle shutdown.
        """

        self.started = False



    def stop(self):
        """
        Alias for shutdown.
        """

        self.shutdown()



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
            "started": self.started,
        }



# Singleton lifecycle manager

lifecycle = PlatformLifecycle()