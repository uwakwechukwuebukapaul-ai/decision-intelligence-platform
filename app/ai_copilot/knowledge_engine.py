from datetime import datetime


class KnowledgeEngine:
    """
    Security knowledge retrieval layer.
    """


    def search(
        self,
        topic
    ):


        knowledge = {

            "ransomware":
                "Malware that encrypts data and demands payment",

            "phishing":
                "Social engineering attack using fraudulent messages",

            "lateral movement":
                "Attacker movement across internal systems"

        }


        result = knowledge.get(
            topic.lower(),
            "No knowledge entry found"
        )


        return {

            "topic":
                topic,

            "information":
                result,

            "timestamp":
                datetime.utcnow().isoformat()

        }