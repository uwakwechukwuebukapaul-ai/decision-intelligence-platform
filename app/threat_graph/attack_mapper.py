class AttackMapper:


    def map(self, event):

        techniques = []


        text = event.lower()


        if "powershell" in text:

            techniques.append(
                {
                    "technique": "Command and Scripting Interpreter",
                    "id": "T1059"
                }
            )


        if "ransomware" in text or "encrypt" in text:

            techniques.append(
                {
                    "technique": "Data Encrypted for Impact",
                    "id": "T1486"
                }
            )


        return {
            "framework": "MITRE ATT&CK",
            "techniques": techniques,
            "count": len(techniques)
        }