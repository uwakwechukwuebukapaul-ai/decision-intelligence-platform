from datetime import datetime
import hashlib


class CopilotMemory:

    def __init__(self):

        self.sessions = []


    def store(self, interaction):

        memory_id = hashlib.sha256(
            str(interaction).encode()
        ).hexdigest()


        record = {

            "memory_id":
                "COPILOT-" + memory_id[:8],

            "interaction":
                interaction,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.sessions.append(record)


        return record


    def history(self):

        return {

            "count":
                len(self.sessions),

            "sessions":
                self.sessions

        }