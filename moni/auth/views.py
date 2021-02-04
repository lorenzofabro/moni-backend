from .serializers import ObtenerTokenSerializer

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtenerTokenAPIView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ObtenerTokenSerializer