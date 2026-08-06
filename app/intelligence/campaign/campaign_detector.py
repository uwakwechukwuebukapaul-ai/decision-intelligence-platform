"""
Sentinel DNA - Campaign Detector

Detects relationships between
multiple threat indicators.
"""


class CampaignDetector:


    def detect(
        self,
        intelligence_items: list[dict],
    ):


        indicators = []


        techniques = []


        reasons = []



        for item in intelligence_items:


            if item.get(
                "indicator"
            ):

                indicators.append(
                    item["indicator"]
                )


            for technique in item.get(
                "mitre_mapping",
                []
            ):

                techniques.append(
                    technique
                )



        confidence = 0


        if len(indicators) > 1:

            confidence += 40

            reasons.append(
                "Multiple related indicators detected"
            )



        if techniques:

            confidence += 30

            reasons.append(
                "Shared MITRE techniques identified"
            )



        return {

            "campaign_detected":
                confidence >= 50,


            "confidence":
                confidence,


            "indicators":
                indicators,


            "techniques":
                techniques,


            "reasoning":
                reasons,

        }