"""
Sentinel DNA Offline Threat Intelligence Provider

Local intelligence engine.
"""


class OfflineThreatProvider:



    SUSPICIOUS_TLDS = [
        ".xyz",
        ".top",
        ".click",
        ".zip",
        ".ru",
    ]



    def analyze(
        self,
        ioc: str,
    ):


        score = 0

        reasons = []


        for tld in self.SUSPICIOUS_TLDS:

            if ioc.endswith(tld):

                score += 70

                reasons.append(
                    f"Suspicious TLD detected: {tld}"
                )



        if score >= 70:

            level = "high"

        elif score >= 40:

            level = "medium"

        else:

            level = "low"



        return {

            "ioc":
                ioc,

            "reputation_score":
                score,

            "threat_level":
                level,

            "reasons":
                reasons,

            "source":
                "offline_engine",

        }