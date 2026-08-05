class AssetModel:
    """
    Represents organizational assets.

    Tracks:
    - endpoints
    - servers
    - applications
    - criticality
    """


    def register(
        self,
        asset_name,
        asset_type,
        criticality="medium"
    ):

        return {

            "status": "asset_registered",

            "asset": {

                "name": asset_name,

                "type": asset_type,

                "criticality": criticality

            }

        }


    def inventory(
        self,
        assets=None
    ):

        return {

            "total_assets": len(assets or []),

            "assets": assets or []

        }