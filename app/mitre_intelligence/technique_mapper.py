from datetime import datetime


class TechniqueMapper:


    def map(self, event):

        techniques = []


        if "powershell" in event.lower():

            techniques.append(
                {
                    "id": "T1059.001",
                    "name": "PowerShell",
                    "category": "Command and Scripting Interpreter"
                }
            )


        if "ransomware" in event.lower():

            techniques.append(
                {
                    "id": "T1486",
                    "name": "Data Encrypted for Impact",
                    "category": "Impact"
                }
            )


        return {

            "techniques":
                techniques,

            "timestamp":
                datetime.utcnow().isoformat()
        }