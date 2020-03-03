"""Autos views."""


#Django's imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

#Local's imports
from autos.model import Auto



@api_view(['GET'])
def hello_world(request):

    context = {
        "message":'Hello World'
    }
    return Response(context)

