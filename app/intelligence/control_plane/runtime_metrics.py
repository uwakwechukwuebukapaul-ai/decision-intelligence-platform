"""
Runtime Metrics

Collects intelligence execution metrics.
"""

from datetime import UTC, datetime


class RuntimeMetrics:
    def __init__(self):
        self.executions = 0

    def record_execution(self):
        self.executions += 1

    def get_metrics(self):
        return {
            "executions": self.executions,
            "timestamp": datetime.now(UTC).isoformat(),
        }