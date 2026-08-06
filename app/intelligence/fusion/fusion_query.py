"""
Sentinel DNA - Fusion Query Layer
"""


class FusionQuery:
    """
    Query intelligence fusion results.
    """



    def __init__(
        self,
        store,
    ):

        self.store = store



    def search(
        self,
        indicator: str,
    ):

        return [

            item

            for item in self.store.all()

            if item.get(
                "indicator"
            )
            ==
            indicator

        ]