from datetime import datetime


class LessonsLearned:

    def generate(self, incident):

        return {
            "improvements": [
                "Improve detection coverage",
                "Review security controls",
                "Update response playbooks",
                "Enhance monitoring"
            ],
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }