from datetime import datetime


class AssetMapper:


    def map(self,event):

        return {

            "assets":[

                {

                "name":
                "Finance Database Server",

                "criticality":
                "high"

                }

            ],

            "timestamp":
            datetime.utcnow().isoformat()

        }