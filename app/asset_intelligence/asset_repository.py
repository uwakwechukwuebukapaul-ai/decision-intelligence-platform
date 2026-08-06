class AssetRepository:

    def __init__(self):
        self.assets = []


    def save(self, asset):

        self.assets.append(asset)

        return asset


    def get_all(self):

        return self.assets