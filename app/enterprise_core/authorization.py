from datetime import datetime


class Authorization:


    def authorize(self, role):

        permissions = {


            "admin":

            [
                "read",
                "write",
                "execute"
            ],


            "analyst":

            [
                "read",
                "investigate"
            ],


            "viewer":

            [
                "read"
            ]

        }


        return {

            "role":

                role,


            "permissions":

                permissions.get(
                    role,
                    []
                ),


            "timestamp":

                datetime.utcnow().isoformat()
        }