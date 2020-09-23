from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sejaparceiro', views.sejaparceiro, name='sejaparceiro'),
    path('quemsomos', views.quemsomos, name='quemsomos'),
    path('cadastrocliente', views.cadastrocliente, name='cadastrocliente'),
    path('cadastrogestor', views.cadastrogestor, name='cadastrogestor'),
]
