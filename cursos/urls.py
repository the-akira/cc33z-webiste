from . import views
from django.urls import path

urlpatterns = [
    path('', views.CursoList.as_view(), name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('<slug:slug>/', views.CursoDetail.as_view(), name='curso_detalhes'),
]