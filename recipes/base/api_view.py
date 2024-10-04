from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseAPIView(APIView):

    def get_exception_handler(self):
        # default_handler = super().get_exception_handler()

        def handle_exception(exc, context):
            if isinstance(exc, APIException):
                return Response(
                    {
                        'success': False,
                        'code': exc.default_code,
                        'message': exc.default_code,
                    },
                    status=exc.status_code)

            return Response(
                {
                    'success': False,
                    'code': exc.default_code,
                    'message': exc.default_detail,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return handle_exception
