class AttackDatabase:


    def __init__(self):

        self.techniques = {

            "powershell": {
                "id": "T1059.001",
                "name": "PowerShell",
                "tactic": "Execution"
            },

            "command shell": {
                "id": "T1059",
                "name": "Command and Scripting Interpreter",
                "tactic": "Execution"
            },

            "ransomware": {
                "id": "T1486",
                "name": "Data Encrypted for Impact",
                "tactic": "Impact"
            },

            "encryption": {
                "id": "T1486",
                "name": "Data Encrypted for Impact",
                "tactic": "Impact"
            },

            "credential": {
                "id": "T1003",
                "name": "OS Credential Dumping",
                "tactic": "Credential Access"
            }

        }



    def search(self, keyword):

        return self.techniques.get(
            keyword.lower()
        )