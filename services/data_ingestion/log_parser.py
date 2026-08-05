class LogParser:
    """
    Security log parser abstraction.

    Supports future:
    - Windows Events
    - Linux logs
    - Firewall logs
    - Cloud logs
    """

    def parse(self, raw_log):

        return {
            "parsed": True,
            "message": raw_log
        }