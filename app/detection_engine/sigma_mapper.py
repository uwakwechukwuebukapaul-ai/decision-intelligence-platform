from datetime import datetime


class SigmaMapper:


    def map(self,event):

        techniques=[]


        if "PowerShell" in event:

            techniques.append(
                "T1059.001 PowerShell"
            )


        if "ransomware" in event.lower():

            techniques.append(
                "T1486 Data Encrypted for Impact"
            )


        return {

            "framework":
                "Sigma",

            "mapped_detection":
                techniques,

            "timestamp":
                datetime.utcnow().isoformat()

        }