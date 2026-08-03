class AccessControl:



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
            "execute"

        ],


        "viewer":
        [

            "read"

        ]

    }



    def check_permission(
        self,
        role,
        action
    ):


        allowed = self.permissions.get(
            role,
            []
        )


        return {


            "allowed":
                action in allowed,


            "role":
                role,


            "action":
                action

        }