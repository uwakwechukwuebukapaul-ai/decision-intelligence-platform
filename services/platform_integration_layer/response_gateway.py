class ResponseGateway:

    def execute_response(self, action):

        return {
            "action": action,
            "response": "executed",
            "status": "completed"
        }