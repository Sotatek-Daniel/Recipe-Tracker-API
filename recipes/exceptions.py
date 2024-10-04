from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    import pdb
    pdb.set_trace()
    response = exception_handler(exc, context)
    print(response)

    if isinstance(exc, APIException):
        custom_response_data = {
            'code': exc.default_code,
            'details': exc.default_detail,
        }
        return Response(custom_response_data, status=exc.status_code)

    custom_response_data = {
        'code': "InternalServerError",
        'details': "Internal Server Error",
    }
    return Response(custom_response_data,
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
