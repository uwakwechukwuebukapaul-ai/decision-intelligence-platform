from datetime import datetime
import uuid

from .asset_repository import AssetRepository
from .risk_calculator import AssetRiskCalculator



class AssetEngine:


    def __init__(self):

        self.repository = AssetRepository()

        self.risk = AssetRiskCalculator()



    def register_asset(
        self,
        hostname,
        asset_type,
        owner,
        criticality
    ):


        asset = {

            "asset_id":
            "AST-" + uuid.uuid4().hex[:8].upper(),

            "hostname": hostname,

            "asset_type": asset_type,

            "owner": owner,

            "criticality": criticality,

            "created_at":
            datetime.utcnow().isoformat()

        }


        asset["risk"] = self.risk.calculate(asset)


        self.repository.save(asset)


        return asset