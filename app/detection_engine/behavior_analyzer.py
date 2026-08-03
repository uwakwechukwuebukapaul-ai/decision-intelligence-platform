from datetime import datetime


class BehaviorAnalyzer:


    def analyze(self,event):

        text=str(event).lower()


        suspicious=False


        indicators=[

            "ransomware",
            "powershell",
            "credential",
            "lateral movement"

        ]


        detected=[]


        for item in indicators:

            if item in text:

                suspicious=True
                detected.append(item)


        return {

            "suspicious_behavior":suspicious,

            "indicators":detected,

            "timestamp":datetime.utcnow().isoformat()

        }