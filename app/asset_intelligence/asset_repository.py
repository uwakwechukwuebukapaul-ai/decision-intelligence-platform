"""
Sentinel DNA Asset Repository

Temporary persistence layer.
"""


class AssetRepository:


    def __init__(self):

        self.assets = {}



    def save(
        self,
        asset
    ):

        self.assets[
            asset["asset_id"]
        ] = asset


        return asset



    def get(
        self,
        asset_id
    ):

        return self.assets.get(
            asset_id
        )



    def list_assets(
        self
    ):

        return list(
            self.assets.values()
        )