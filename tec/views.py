from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'amapatec/pages/home.html', context={'title': 'Associação Amapaense de Tecnologia'})

def institucional(request):
    return render(request, 'amapatec/pages/institucional.html', context={'title': 'Institucional'})

def projetos(request):
    return render(request, 'amapatec/pages/projetos.html', context={'title': 'Projetos'})

def contato(request):
    return render(request, 'amapatec/pages/contato.html', context={'title': 'Contato'})


def associados(request):
    return render(request, 'amapatec/pages/associados.html', context={'title': 'Associados'})

def beneficios(request):
    return render(request, 'amapatec/pages/beneficios.html', context={'title': 'Benefícios'})


def associese(request):
    return render(request, 'amapatec/pages/associe-se.html', context={'title': 'Associe-se'})


def agendaeventos(request):
    return render(request, 'amapatec/pages/agenda-de-eventos.html', context={'title': 'Agenda de Eventos'})


def associado(request):
    return render(request, 'amapatec/pages/associado.html', context={'title': 'Area de Associado'})





def politicaprivacidade(request):
    return render(request, 'amapatec/pages/politicaprivacidade.html', context={'title': 'Política de Privacidade'})


def maintenance(request):
    return render(request, 'amapatec/pages/maintenance.html', context={'title': 'Associação Amapaense de Tecnologia'})
