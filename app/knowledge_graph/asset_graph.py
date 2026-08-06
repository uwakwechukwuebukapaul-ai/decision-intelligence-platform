class AssetGraph:


    def create_asset_node(self, asset):

        return {
            "asset_id": asset["asset_id"],
            "hostname": asset.get("hostname"),
            "type": asset.get("type")
        }