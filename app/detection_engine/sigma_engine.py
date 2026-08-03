from datetime import datetime


class SigmaEngine:


    def __init__(self):

        self.rules=[

            "Process Injection",

            "Suspicious PowerShell",

            "Credential Dumping",

            "Ransomware Activity"

        ]


    def evaluate(self,event):

        matched=[]


        text=str(event).lower()


        for rule in self.rules:

            keyword=rule.lower().split()[0]


            if keyword in text:

                matched.append(rule)


        return {

            "sigma_matches":matched,

            "count":len(matched),

            "timestamp":datetime.utcnow().isoformat()

        }