from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def foo(request):
    return Response('foo')