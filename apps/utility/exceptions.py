from rest_framework import status
from rest_framework.exceptions import APIException


class ServiceAPIException(APIException):
    def __init__(self, type, message, status_code=status.HTTP_400_BAD_REQUEST):
        self.status_code = status_code
        self.default_detail = {
            "error": {
                "type": type,
                "message": message
            }
        }
        super().__init__()


class ServiceAPIException500(APIException):
    def __init__(self):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.default_detail = {
            "error": {
                "type": "service_error",
                "message": "A service error occured"
            }
        }
        super().__init__()
