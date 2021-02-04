from django.urls import path

from .views import PedidoPrestamoAPIView, PedidoPrestamoDetailAPIView, GeneroAPIView

urlpatterns = [
    path('pedido/', PedidoPrestamoAPIView.as_view()),
    path('pedido/<int:pk>/', PedidoPrestamoDetailAPIView.as_view()),
    path('generos/', GeneroAPIView.as_view()),
]
