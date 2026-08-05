class DataLifecycle:
    """
    Controls security data lifecycle.

    Stages:

    Collection
    Storage
    Usage
    Archive
    Disposal
    """

    def process(self, data):

        return {
            "stage": "stored",
            "data": data
        }