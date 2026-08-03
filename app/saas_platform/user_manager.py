from datetime import datetime
import uuid


class UserManager:

    def create(self, email):

        return {
            "user_id": f"USER-{uuid.uuid4().hex[:8].upper()}",
            "email": email,
            "role": "SOC Analyst",
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }