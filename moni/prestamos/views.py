import requests

from django.conf import settings

from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsPostOrIsAuthenticated

from .models import Genero, PedidoPrestamo
from .serializers import GeneroSerializer, PedidoPrestamoSerializer



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

class GeneroAPIView(generics.ListAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = (AllowAny, )

class PedidoPrestamoAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PedidoPrestamo.objects.all()
    serializer_class = PedidoPrestamoSerializer
    permission_classes = (IsPostOrIsAuthenticated, )
    
    def post(self, request, *args, **kwargs):
        request.data["aprobado"] = validar_prestamo(request.data["dni"])
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PedidoPrestamoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PedidoPrestamo.objects.all()
    serializer_class = PedidoPrestamoSerializer
    permission_class = [IsAuthenticated]
