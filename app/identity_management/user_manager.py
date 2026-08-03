from datetime import datetime


class UserManager:


    def create_user(self, username):

        return {

            "user_id":
                f"USER-{username.upper()}",

            "username":
                username,

            "status":
                "active",

            "created_at":
                datetime.utcnow().isoformat()

        }