from datetime import datetime


class TenantIsolation:


    def configure(self, organization):

        return {

            "isolation":
                "enabled",

            "strategy":
                "Logical tenant data separation",

            "tenant":
                organization,

            "timestamp":
                datetime.utcnow().isoformat()

        }