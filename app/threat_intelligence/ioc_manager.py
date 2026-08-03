from datetime import datetime


class IOCManager:
    """
    Indicator of Compromise management.
    """


    def __init__(self):

        self.iocs = []



    def add_ioc(
        self,
        indicator,
        ioc_type
    ):

        ioc = {

            "indicator":
                indicator,

            "type":
                ioc_type,

            "status":
                "ACTIVE",

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.iocs.append(ioc)

        return ioc



    def search(
        self,
        indicator
    ):

        return [

            ioc
            for ioc in self.iocs
            if indicator in ioc["indicator"]

        ]