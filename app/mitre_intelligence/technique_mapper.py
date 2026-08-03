from datetime import datetime


class TechniqueMapper:


    def map(self, incident):

        techniques = []


        text = incident.lower()


        if "powershell" in text:
            techniques.append({
                "id": "T1059.001",
                "name": "PowerShell",
                "tactic": "Execution"
            })


        if "ransomware" in text or "encrypt" in text:
            techniques.append({
                "id": "T1486",
                "name": "Data Encrypted for Impact",
                "tactic": "Impact"
            })


        if "database" in text:
            techniques.append({
                "id": "T1213",
                "name": "Data from Information Repositories",
                "tactic": "Collection"
            })


        if not techniques:
            techniques.append({
                "id": "T1059",
                "name": "Command and Scripting Interpreter",
                "tactic": "Execution"
            })


        return {
            "framework": "MITRE ATT&CK",
            "count": len(techniques),
            "techniques": techniques,
            "timestamp": datetime.now().isoformat()
        }