
from django.urls import include, path

from tec.views import home, maintenance

urlpatterns = [
    path('', home),
]
