from datetime import datetime


class DataPartition:


    def create(self, organization):

        return {

            "tenant":
                organization,

            "storage":
                "isolated tenant namespace",

            "database_partition":
                "created",

            "timestamp":
                datetime.utcnow().isoformat()

        }