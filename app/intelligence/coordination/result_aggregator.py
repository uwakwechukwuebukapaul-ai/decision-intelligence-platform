"""
Result Aggregator

Collects results from multiple
agent executions into a single
investigation output.
"""

from __future__ import annotations


class ResultAggregator:
    """
    Aggregates execution results.

    The coordinator submits every
    completed job to this class.
    """

    def __init__(self):

        self._results: list[dict] = []

    def add_result(
        self,
        result: dict,
    ) -> None:
        """
        Store a completed result.
        """

        self._results.append(result)

    def results(
        self,
    ) -> list[dict]:
        """
        Return every collected result.
        """

        return list(self._results)

    def successful(
        self,
    ) -> list[dict]:

        return [

            result

            for result in self._results

            if result.get("status") == "completed"

        ]

    def failed(
        self,
    ) -> list[dict]:

        return [

            result

            for result in self._results

            if result.get("status") != "completed"

        ]

    def summary(
        self,
    ) -> dict:

        total = len(self._results)

        success = len(
            self.successful()
        )

        failed = len(
            self.failed()
        )

        return {

            "total": total,

            "successful": success,

            "failed": failed,

        }

    def investigation_result(
        self,
    ) -> dict:
        """
        Final investigation output.

        Future versions can include:

        - timings
        - confidence
        - provenance
        - evidence graph
        - AI reasoning
        """

        return {

            "summary":
                self.summary(),

            "results":
                self.results(),

        }

    def clear(
        self,
    ) -> None:

        self._results.clear()