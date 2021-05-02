from . import views
from django.urls import path

urlpatterns = [
    path('pensamentos/', views.PensamentoList.as_view(), name='pensamentos'),
]