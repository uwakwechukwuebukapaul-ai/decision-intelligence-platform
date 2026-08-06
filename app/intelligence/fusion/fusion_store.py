"""
Sentinel DNA - Fusion Storage Layer
"""


from __future__ import annotations


class FusionStore:
    """
    Stores intelligence fusion results.

    Placeholder for future:

    - SQLite
    - PostgreSQL
    - Elasticsearch
    - Vector database
    """



    def __init__(self):

        self.results = []



    def save(
        self,
        result: dict,
    ):

        self.results.append(
            result
        )

        return result



    def all(self):

        return self.results