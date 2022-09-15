# from webbrowser import get
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from APIapp.models import Item
# from .serializers import ItemSerialiser

# # Create your views here.
# @api_view(['GET'])
# def getData(request):
#     data = Item.objects.all()
#     serializerObj = ItemSerialiser(data,many = True)
#     return Response(serializerObj.data)


# views.py
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase


class SoapService(ServiceBase):
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def hello(ctx, name):
        return 'Hello, {}'.format(name)

    @rpc(Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def sum(ctx, a, b):
        return int(a + b)


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)