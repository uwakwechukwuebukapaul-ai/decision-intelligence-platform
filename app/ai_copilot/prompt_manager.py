from datetime import datetime


class PromptManager:

    def build_prompt(self, request):

        return {
            "prompt":
                f"Analyze cybersecurity request: {request}",
            "type":
                "SOC Investigation Prompt",
            "timestamp":
                datetime.utcnow().isoformat()
        }