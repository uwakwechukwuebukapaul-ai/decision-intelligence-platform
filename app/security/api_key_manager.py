import uuid
from datetime import datetime



class APIKeyManager:



    def __init__(self):

        self.keys = {}



    def generate_key(
        self,
        user_id
    ):


        api_key = (

            "sdna_"
            +
            uuid.uuid4().hex

        )


        self.keys[api_key] = {


            "user_id":
                user_id,


            "created_at":
                datetime.utcnow().isoformat(),


            "active":
                True

        }



        return {


            "status":
                "created",


            "api_key":
                api_key

        }



    def validate_key(
        self,
        api_key
    ):


        key = self.keys.get(
            api_key
        )



        if key and key["active"]:


            return {


                "valid":
                    True,


                "user_id":
                    key["user_id"]

            }



        return {


            "valid":
                False

        }