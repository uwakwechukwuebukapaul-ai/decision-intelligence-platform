"""
Pipeline Result
"""

from __future__ import annotations


class PipelineResult:

    def __init__(
        self,
        response,
        context,
    ):

        self.response = response

        self.context = context

    def to_dict(self):

        return {

            "response":
                self.response.to_dict(),

            "context":
                self.context.to_dict(),

        }