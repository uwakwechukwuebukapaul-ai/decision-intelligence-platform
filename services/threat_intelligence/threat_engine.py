"""
Sentinel DNA Threat Intelligence Engine

Provides:
- threat analysis
- indicator extraction
- reputation scoring
- backward compatibility support
"""


class ThreatEngine:
    """
    Sentinel DNA Threat Intelligence Core Engine
    """

    def __init__(self):
        self.name = "Threat Intelligence Engine"
        self.version = "1.0"


    def analyze(self, indicator):
        """
        Analyze threat intelligence input.

        Maintains Sentinel DNA legacy response contract.
        """

        threat_keywords = [
            "ransomware",
            "powershell",
            "malware",
            "attack",
            "phishing",
            "exploit",
            "credential",
            "breach"
        ]


        matches = [
            keyword
            for keyword in threat_keywords
            if keyword.lower() in indicator.lower()
        ]


        risk = "high" if matches else "low"


        return {
            "status": "threat_intelligence_processed",

            "indicator": indicator,


            # Legacy compatibility
            "indicators": matches,


            # New Sentinel DNA naming
            "matched_threats": matches,


            "risk": risk,


            # Legacy reputation contract
            "reputation": {
                "risk_level": risk.upper(),
                "confidence": 0.95 if matches else 0.40,
                "classification": (
                    "malicious"
                    if matches
                    else "unknown"
                )
            },


            "source": self.name,

            "version": self.version
        }



    def enrich(self, intelligence):
        """
        Add intelligence enrichment data.
        """

        return {
            "status": "completed",
            "enrichment": intelligence,
            "engine": self.name
        }



    def get_threat_context(self, threat):
        """
        Generate adversary context.
        """

        return {
            "threat": threat,
            "classification": "unknown",
            "confidence": 0.5
        }



    def health(self):
        """
        Engine health status.
        """

        return {
            "engine": self.name,
            "version": self.version,
            "status": "healthy"
        }



# Backward compatibility alias
# Existing Sentinel DNA modules use this name
ThreatIntelligenceEngine = ThreatEngine