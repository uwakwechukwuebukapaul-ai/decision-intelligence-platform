"""
Sentinel DNA Threat Intelligence Agent

Responsible for:

- IOC enrichment foundation
- Threat indicator analysis
- Reputation scoring
- Intelligence confidence calculation
"""

from .base_agent import BaseAgent


class ThreatIntelligenceAgent(BaseAgent):
    """
    Threat intelligence analysis agent.

    Future integrations:
    - VirusTotal
    - AbuseIPDB
    - MISP
    - OpenCTI
    - Internal threat feeds
    """

    def __init__(self):

        super().__init__(
            "ThreatIntelligenceAgent"
        )


    def analyze(
        self,
        investigation
    ):

        findings = []

        evidence = investigation.evidence


        if not evidence:

            findings.append(
                "No indicators available for intelligence analysis"
            )


        else:

            for indicator in evidence:

                findings.append(
                    self.analyze_indicator(
                        indicator
                    )
                )


        confidence = self.calculate_confidence(
            findings
        )


        result = {

            "agent":
                self.name,

            "findings":
                findings,

            "confidence":
                confidence
        }


        for finding in findings:

            investigation.add_finding(
                finding
            )


        return result



    def analyze_indicator(
        self,
        indicator
    ):

        value = str(
            indicator
        ).lower()


        threat_patterns = [

            "malicious",
            "phishing",
            "payload",
            "trojan",
            "virus",
            "ransomware",
            "domain",
            "command",
            "control",
            "c2"

        ]


        for pattern in threat_patterns:

            if pattern in value:

                return {

                    "indicator":
                        indicator,

                    "classification":
                        "SUSPICIOUS",

                    "reason":
                        f"Matched threat pattern: {pattern}",

                    "severity":
                        "HIGH"

                }


        return {

            "indicator":
                indicator,

            "classification":
                "UNKNOWN",

            "reason":
                "No threat intelligence match found",

            "severity":
                "LOW"

        }



    def calculate_confidence(
        self,
        findings
    ):

        if not findings:

            return 0


        suspicious = 0


        for finding in findings:

            if (
                isinstance(
                    finding,
                    dict
                )
                and finding.get(
                    "classification"
                )
                == "SUSPICIOUS"
            ):

                suspicious += 1


        confidence = (
            suspicious /
            len(findings)
        ) * 100


        return round(
            confidence,
            2
        )