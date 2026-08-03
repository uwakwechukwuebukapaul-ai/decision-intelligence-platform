from functools import wraps



class SecurityMiddleware:



    def __init__(
        self,
        api_key_manager
    ):

        self.api_key_manager = (
            api_key_manager
        )



    def require_api_key(
        self,
        function
    ):


        @wraps(function)

        def wrapper(
            *args,
            **kwargs
        ):


            api_key = kwargs.get(
                "api_key"
            )



            validation = (
                self.api_key_manager
                .validate_key(api_key)
            )



            if not validation["valid"]:


                return {


                    "error":
                        "Unauthorized access"

                }



            return function(
                *args,
                **kwargs
            )


        return wrapper