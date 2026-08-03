class MITREMapper:


    def map_attack(
        self,
        indicators
    ):


        techniques = []


        for item in indicators:


            text = item.lower()


            if "phishing" in text:

                techniques.append({

                    "technique":
                        "Phishing",

                    "mitre_id":
                        "T1566"

                })


            if "credential" in text:

                techniques.append({

                    "technique":
                        "Credential Access",

                    "mitre_id":
                        "TA0006"

                })


            if "malware" in text:

                techniques.append({

                    "technique":
                        "Malware",

                    "mitre_id":
                        "T1204"

                })



        return {


            "mapped_techniques":
                techniques,


            "count":
                len(techniques)

        }