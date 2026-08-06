class EvidenceCorrelator:


    def correlate(self, evidence):

        findings=[]


        for item in evidence:

            if item["type"]=="IOC":
                findings.append(
                    "Malicious indicator evidence found"
                )


            if item["type"]=="IDENTITY":
                findings.append(
                    "Identity context evidence found"
                )


            if item["type"]=="ASSET":
                findings.append(
                    "Asset context evidence found"
                )


        return findings