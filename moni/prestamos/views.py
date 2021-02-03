import requests

from django.http.response import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework import serializers, status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import PedidoPrestamo
from .serializers import PedidoPrestamoSerializer


def validar_prestamo(dni: int):
    BASE_URL = 'https://api.moni.com.ar/api/v4/scoring/pre-score'
    API_KEY = settings.MONI_API_KEY
    url_request = f"{BASE_URL}/{dni}"
    try:
        response = requests.get(url_request, headers={'credential': API_KEY})
        if response.status_code == requests.status_codes.codes.ok:
            data = response.json()
            if data["has_error"]:
                raise Exception("Ha ocurrido un error en la verificación del prestamo")
            return data['status'] == 'approve' # Cualquier resultado que fuese diferente a "approve" se considerará rechazado
    except Exception as e:
        raise e


class PedidoPrestamoAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PedidoPrestamo.objects.all()
    serializer_class = PedidoPrestamoSerializer
    
    def post(self, request, *args, **kwargs):
        request.data["aprobado"] = validar_prestamo(request.data["dni"])
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PedidoPrestamoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PedidoPrestamo.objects.all()
    serializer_class = PedidoPrestamoSerializer
