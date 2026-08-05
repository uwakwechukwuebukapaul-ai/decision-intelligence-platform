class PlaybookGenerator:
    """
    Generates automated SOC response playbooks.
    """

    def generate(
        self,
        threat
    ):

        threat_lower = threat.lower()


        playbook = []


        if "ransomware" in threat_lower:

            playbook.extend([
                "isolate affected hosts",
                "disable compromised accounts",
                "collect forensic evidence",
                "restore from clean backups"
            ])


        elif "phishing" in threat_lower:

            playbook.extend([
                "block malicious domain",
                "quarantine email",
                "reset affected credentials"
            ])


        elif "powershell" in threat_lower:

            playbook.extend([
                "collect PowerShell logs",
                "inspect execution history",
                "hunt related commands"
            ])


        else:

            playbook.append(
                "perform analyst investigation"
            )


        return playbook