from datetime import datetime, timezone

from services.observability.service_registry import ServiceRegistry
from services.observability.health_monitor import HealthMonitor
from services.observability.metrics_engine import MetricsEngine
from services.observability.execution_trace import ExecutionTrace


class ObservabilityManager:

    def __init__(self):

        self.registry = ServiceRegistry()
        self.health = HealthMonitor()
        self.metrics = MetricsEngine()
        self.trace = ExecutionTrace()


    def register_service(
        self,
        name,
        service=None
    ):

        registered = self.registry.register(
            name,
            service
        )

        self.health.check(
            self.registry
        )

        return registered


    def start_execution(
        self,
        name
    ):

        self.metrics.record_execution(
            name
        )

        return self.trace.start(
            name
        )


    def complete_execution(
        self,
        name,
        success=True
    ):

        self.metrics.record_result(
            name,
            success
        )

        return self.trace.complete(
            name
        )


    def report(self):

        return {

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "services":
                self.registry.services,

            "health":
                self.health.status(),

            "metrics":
                self.metrics.metrics,

            "trace":
                self.trace.events
        }