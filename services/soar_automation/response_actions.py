class ResponseActions:
    """
    Security response action library.
    """

    def available(self):

        return [
            "block_ip",
            "disable_account",
            "isolate_host",
            "collect_evidence",
            "create_ticket",
            "notify_analyst"
        ]

    def block_ip(self, ip):

        return {
            "action": "block_ip",
            "target": ip,
            "status": "queued"
        }

    def isolate_host(self, host):

        return {
            "action": "isolate_host",
            "target": host,
            "status": "queued"
        }