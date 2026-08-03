from datetime import datetime

from .authentication import Authentication
from .authorization import Authorization
from .request_validator import RequestValidator
from .response_formatter import ResponseFormatter
from .api_logger import APILogger
from .gateway_memory import GatewayMemory


class APIGatewayEngine:

    def __init__(self):

        self.authentication = Authentication()
        self.authorization = Authorization()
        self.validator = RequestValidator()
        self.formatter = ResponseFormatter()
        self.logger = APILogger()
        self.memory = GatewayMemory()


    def process_request(self, request_type, payload):

        auth = self.authentication.validate()

        permission = self.authorization.check(
            request_type
        )

        validation = self.validator.validate(
            payload
        )

        memory = self.memory.store(
            request_type,
            payload
        )

        log = self.logger.record(
            request_type
        )


        response = {

            "request_type": request_type,

            "payload": payload,

            "authentication": auth,

            "authorization": permission,

            "validation": validation,

            "memory": memory,

            "log": log,

            "processed_at":
                datetime.utcnow().isoformat()

        }


        return self.formatter.success(
            response
        )