from datetime import datetime


class SignatureEngine:


    def detect(self,event):

        signatures=[

            "malware",
            "trojan",
            "ransomware",
            "backdoor"

        ]


        matched=[]


        text=str(event).lower()


        for signature in signatures:

            if signature in text:

                matched.append(signature)


        return {

            "signatures_found":matched,

            "count":len(matched),

            "timestamp":datetime.utcnow().isoformat()

        }