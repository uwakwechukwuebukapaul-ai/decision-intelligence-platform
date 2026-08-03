from datetime import datetime


class BehaviorHunter:


    def search(self, intelligence):


        indicators=[]


        text=str(intelligence).lower()


        behaviours=[

            "credential theft",

            "lateral movement",

            "privilege escalation",

            "data encryption"

        ]


        for item in behaviours:

            if item.split()[0] in text:

                indicators.append(item)



        return {

            "behaviors_detected":
                indicators,

            "count":
                len(indicators),

            "timestamp":
                datetime.utcnow().isoformat()

        }