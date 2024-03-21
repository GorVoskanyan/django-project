from rest_framework.decorators import api_view
from rest_framework import Response
from rest_framework import Request


@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({"message": 'Hello World'})