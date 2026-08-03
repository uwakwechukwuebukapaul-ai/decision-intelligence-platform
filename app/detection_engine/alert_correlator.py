from datetime import datetime


class AlertCorrelator:


    def correlate(self,data):

        findings=[]


        if data["rules"]["count"] > 0:

            findings.append(
                "Rule based detection triggered"
            )


        if data["anomaly_analysis"]["anomaly"]:

            findings.append(
                "Behavior anomaly detected"
            )


        severity="low"


        if len(findings)>=2:

            severity="high"


        return {

            "correlated_findings":findings,

            "severity":severity,

            "timestamp":datetime.utcnow().isoformat()

        }