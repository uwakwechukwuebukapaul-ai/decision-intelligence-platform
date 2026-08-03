from datetime import datetime


class LessonsLearned:


    def generate(self, incident):

        return {

            "review_points": [

                "Analyze attack entry point",

                "Improve detection coverage",

                "Update incident response playbooks",

                "Strengthen security controls"

            ],

            "incident":
                incident,

            "status":
                "generated",

            "timestamp":
                datetime.utcnow().isoformat()

        }