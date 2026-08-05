class IntelligenceRouter:


    def route(self, context):

        return {
            "destination": "security_intelligence_os",
            "priority": "normal",
            "context": context
        }