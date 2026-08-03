from datetime import datetime


class AttackMapper:


    def map(self, intelligence):


        text=str(intelligence).lower()


        techniques=[]


        if "ransomware" in text:

            techniques.append(
                {
                    "technique":
                    "Data Encrypted for Impact",
                    "id":
                    "T1486"
                }
            )


        if "phishing" in text:

            techniques.append(
                {
                    "technique":
                    "Phishing",
                    "id":
                    "T1566"
                }
            )


        return {

            "techniques": techniques,

            "count": len(techniques),

            "framework":
                "MITRE ATT&CK",

            "timestamp":
                datetime.utcnow().isoformat()

        }