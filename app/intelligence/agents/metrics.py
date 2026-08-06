"""
Agent Metrics
"""


class AgentMetrics:

    def __init__(self):

        self.executions = 0

        self.failures = 0

    def record_success(self):

        self.executions += 1

    def record_failure(self):

        self.executions += 1

        self.failures += 1

    def summary(self):

        return {

            "executions":
                self.executions,

            "failures":
                self.failures,

            "successes":
                self.executions - self.failures,

        }