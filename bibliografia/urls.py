from . import views
from django.urls import path

urlpatterns = [
    path('livros/', views.LivroList.as_view(), name='livros'),
]