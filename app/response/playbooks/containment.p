class ContainmentPlaybook:



    def block_indicator(
        self,
        incident_id
    ):

        return {

            "action":
                "indicator_blocked",

            "incident_id":
                incident_id,

            "result":
                "IOC added to block list"

        }



    def collect_telemetry(
        self,
        incident_id
    ):

        return {

            "action":
                "telemetry_collection",

            "incident_id":
                incident_id,

            "result":
                "Endpoint telemetry requested"

        }