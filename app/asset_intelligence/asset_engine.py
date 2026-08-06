"""
Sentinel DNA Asset Intelligence Engine

Tracks enterprise assets and risk context.
"""


from .asset_schema import create_asset
from .asset_repository import AssetRepository



class AssetEngine:


    def __init__(self):

        self.repository = AssetRepository()



    def register_asset(
        self,
        hostname,
        ip_address=None,
        owner=None,
        asset_type="endpoint",
        criticality="medium"
    ):


        asset = create_asset(

            hostname,

            ip_address,

            owner,

            asset_type,

            criticality

        )


        return self.repository.save(
            asset
        )



    def get_asset(
        self,
        asset_id
    ):

        return self.repository.get(
            asset_id
        )



    def inventory(
        self
    ):

        return self.repository.list_assets()