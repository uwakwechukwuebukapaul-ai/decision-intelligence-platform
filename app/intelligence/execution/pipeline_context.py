"""
Pipeline Context

Shared execution state.
"""

from __future__ import annotations


class PipelineContext:

    def __init__(self):

        self.values: dict = {}

    def set(
        self,
        key,
        value,
    ):

        self.values[key] = value

    def get(
        self,
        key,
        default=None,
    ):

        return self.values.get(
            key,
            default,
        )

    def to_dict(self):

        return dict(self.values)