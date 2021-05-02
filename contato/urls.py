from . import views
from django.urls import path

urlpatterns = [
    path('contato/', views.contato, name='contato'),
]