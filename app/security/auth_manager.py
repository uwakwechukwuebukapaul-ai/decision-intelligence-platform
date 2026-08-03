from datetime import datetime
import uuid
import hashlib



class AuthManager:


    def __init__(self):

        self.users = {}



    def create_user(
        self,
        username,
        password
    ):


        user_id = (
            "USER-" +
            uuid.uuid4().hex[:8].upper()
        )


        password_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()



        self.users[user_id] = {


            "user_id":
                user_id,


            "username":
                username,


            "password_hash":
                password_hash,


            "role":
                "analyst",


            "created_at":
                datetime.utcnow().isoformat()

        }



        return {


            "status":
                "created",


            "user":
                self.users[user_id]

        }



    def authenticate(
        self,
        username,
        password
    ):


        password_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()



        for user in self.users.values():


            if (
                user["username"] == username
                and
                user["password_hash"] == password_hash
            ):


                return {


                    "status":
                        "authenticated",


                    "user_id":
                        user["user_id"],


                    "role":
                        user["role"]

                }



        return {


            "status":
                "failed"

        }