from enum import IntEnum

class RequestType(IntEnum):
    POST = 1
    GET = 2

request_type = RequestType.POST
print(request_type)
