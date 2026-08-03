from datetime import datetime


class IOCHunter:


    def search(self, intelligence):


        text=str(intelligence)


        found=[]


        indicators=[

            "ip",

            "domain",

            "hash",

            "malware"

        ]


        for item in indicators:

            if item in text.lower():

                found.append(item)



        return {

            "ioc_types_found":
                found,

            "count":
                len(found),

            "timestamp":
                datetime.utcnow().isoformat()

        }