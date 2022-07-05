from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import time

@api_view(['GET'])
def say_hello(request):
    message = 'Hello World'
    return Response(message, status=HTTP_200_OK)


@api_view(['POST'])
def say_my_name(request):
    name = request.data.get('name', 'anonymous ')
    message = f'Hello {name}'
    return Response(message, status=HTTP_200_OK)


@api_view(['GET'])
def readiness(request):
    return Response({'message': 'ok'}, status=200)


@api_view(['GET'])
def liveness(request):
     time.sleep(15)
    return Response({'message': 'ok'}, status=200)
