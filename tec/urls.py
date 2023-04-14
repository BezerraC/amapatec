
from django.urls import path, include
from tec.views import home
urlpatterns = [
    path('', home),
]
