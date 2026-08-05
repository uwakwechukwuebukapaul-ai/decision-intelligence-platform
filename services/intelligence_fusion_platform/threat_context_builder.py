class ThreatContextBuilder:
    """
    Builds unified threat context.
    """


    def build(
        self,
        event,
        intelligence,
        mitre,
        iocs
    ):

        return {

            "event": event,

            "threat_intelligence":
                intelligence,

            "mitre_context":
                mitre,

            "ioc_context":
                iocs
        }