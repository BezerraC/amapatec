from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'amapatec/pages/home.html', context={'title': 'Associação Amapaense de Tecnologia'})


def maintenance(request):
    return render(request, 'amapatec/pages/maintenance.html', context={'title': 'Associação Amapaense de Tecnologia'})
