class CopilotEngine:
    """
    AI SOC analyst assistant.
    """

    def __init__(self):
        self.requests = []


    def analyze_alert(self, alert):

        result = {
            "alert": alert,
            "summary": "AI generated security analysis",
            "recommendation": "Investigate related entities"
        }

        self.requests.append(result)

        return result


    def explain(self, context):

        return {
            "explanation": context
        }