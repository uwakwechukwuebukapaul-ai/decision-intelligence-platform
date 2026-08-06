class CorrelationEngine:


    def correlate(self, event):

        signals = []


        if event.get("indicator"):
            signals.append("IOC correlated")


        if event.get("asset"):
            signals.append("Asset context correlated")


        if event.get("identity"):
            signals.append("Identity context correlated")


        return signals