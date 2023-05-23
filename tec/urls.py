
from django.urls import include, path

from tec.views import *

urlpatterns = [
    path('', home),
    path('institucional/', institucional),
    path('projetos/', projetos),
    path('contato/', contato),
    path('associados/', associados),
    path('associe-se/', associese),
    path('associado/', associado),
    path('beneficios/', beneficios),
    path('agenda-de-eventos/', agendaeventos),
    path('politica-de-privacidade/', politicaprivacidade),
]
